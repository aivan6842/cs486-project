from argparse import ArgumentParser
import json
import pandas 
from inference.infer import inference
from evaluation.metrics.mean_reciprocal_rank import MeanReciprocalRank 
from evaluation.metrics.generalized_MRR import GeneralizedMeanReciprocalRank 

def evaluate(file: str, retriever_names: list, metric_name: str, is_long_query:bool , rerank: bool=False, reranker: str='minilm'):
    METRIC_MAP = {
        "MRR" : MeanReciprocalRank,
        "GMRR" : GeneralizedMeanReciprocalRank,

    }
    #f=open(file,'r')
    df=pandas.read_excel(file)
    #row=f.readlines()
    res=[]#is gonna contain query, y_hat and y
    for i,row in df.iterrows():
        query=row['Bio'] if is_long_query else row['query']
        y=[]
        for i in range(1,11):
            y.append(row[f'course_code{i}'])
        y_hat=inference(query=query,retriever_names=retriever_names,k=10,rerank=rerank,ranker=reranker)
        y_hat_course_codes=[x[0] for x in y_hat]
        res.append((query,y,y_hat_course_codes))
    

    metric=METRIC_MAP[metric_name]()
    return metric.evaluate(y=[x[1] for x in res],y_hat=[x[2] for x in res])



if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-f", "--file",
                        type=str,
                        help="Path to test data",
                        required=True)
    parser.add_argument("-rt", "--retrievers",
                        type=str,
                        nargs="*",
                        default=["BM25"],
                        help="list of retrievers",
                        required=True)
    parser.add_argument("-m", "--metric",
                        type=str,
                        help="metric",
                        required=True)
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
    parser.add_argument("-l", "--differentiate",
                        type=bool,
                        help="Long (true) or Short (false) query?",
                        required=True)
    
    args = parser.parse_args()

    res = evaluate( file=args.file,
                    retriever_names=args.retrievers,
                    metric_name=args.metric,
                    is_long_query=args.differentiate,
                    rerank=args.rerank,
                    reranker=args.ranker
                    )
    print("res:",res)   
