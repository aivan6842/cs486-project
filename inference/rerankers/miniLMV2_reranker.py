from sentence_transformers import CrossEncoder

from inference.rerankers.reranker import Reranker

class MiniLMV2Reranker(Reranker):

    def __init__(self) -> None:
        self.model_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
        self.model = CrossEncoder(self.model_name, max_length=512)

    
    def rerank(self, data: list[tuple[str, str, str]], query: str) -> list[tuple[str, str, str]]:
        # data = [(course code, course name, course description)]
        pairs = [(query, doc[2]) for doc in data]
        scores = self.model.predict(pairs)

        # merge scores with data to sort
        scored_data = [(data[i], scores[i]) for i in range(len(scores))]

        sorted_data = sorted(scored_data, key = lambda x : x[1], reverse=True)
        sorted_data = [item[0] for item in sorted_data]

        return sorted_data
