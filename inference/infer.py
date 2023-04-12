from argparse import ArgumentParser

from inference.retrievers.bm25_retriever import BM25Retriever
from inference.retrievers.dpr_retriever import DPRRetriever
from inference.retrievers.t5_retriever import T5Retriever
from inference.rerankers.miniLMV2_reranker import MiniLMV2Reranker
from inference.rerankers.BERT_reranker import BERTReranker
from inference.rerankers.ELECTRA_reranker import ELECTRAReranker

def inference(query: str, retriever_names: list, k: int = 5, rerank: bool = False, ranker: str = 'minilm') -> list[tuple[str, str, str]]:
    """
    Given a list of retrievers will return top k course suggestions
    Returns : [(course_code, course_name, course_description), ...]
    """
    RETRIEVER_MAP = {
        "bm25" : BM25Retriever,
        "dpr" : DPRRetriever,
        "t5": T5Retriever
    }

    # Init retrievers
    retrievers = [RETRIEVER_MAP[retriever.lower()]() for retriever in list(set(retriever_names))]

    unranked_res = []
    for retriever in retrievers:
        retrieved_res = retriever.retrieve(query=query, num_results=k)
        # unpack es result
        for item in retrieved_res["hits"]["hits"]:
            source_item = item["_source"]
            unranked_res.append((source_item["courseCode"], source_item["courseName"], source_item["courseDescription"]))

    # If only a single retrieved was used, then results are already ranked by es
    # If rerank was enabled for a single retriever, then results are also reranked by reranker
    # If multiple retrievers are used, then all results are ranked by reranker regardless of rerank param
    if len(retriever_names) > 1:
        rerank = True
    
    RERANKER_MAP = {
        "minilm" : MiniLMV2Reranker,
        "bert" : BERTReranker,
        "electra": T5Retriever
    }

    # unique results only
    reranked_res = list(set(unranked_res))
    if rerank:
        reranker = RERANKER_MAP[ranker]()
        reranked_res = reranker.rerank(data=reranked_res, query=query)
    
    return reranked_res[:k]


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-q", "--query",
                        type=str,
                        help="Query",
                        required=True)
    parser.add_argument("-rt", "--retrievers",
                        type=str,
                        nargs="*",
                        default=["BM25"],
                        help="list of retrievers",
                        required=True)
    parser.add_argument("-n", "--num_results",
                        type=int,
                        default=5,
                        help="number of documents retrieved during inference",
                        required=False)
    parser.add_argument("-rr", "--rerank",
                        type=bool,
                        default=False,
                        help="Rerank documents using re-ranker. Automatically enabled if more than 1 retriever",
                        required=False)
    parser.add_argument("-ra", "--ranker",
                        type=str,
                        default='minilm',
                        help="type of re-ranker. Automatically enabled if more than 1 retriever",
                        required=False)
    
    args = parser.parse_args()

    res = inference(query=args.query, 
              retriever_names=args.retrievers, 
              k=args.num_results,
              rerank=args.rerank,
              ranker=args.ranker)
    
    print(res)

    