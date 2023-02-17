from sentence_transformers import SentenceTransformer
from typing import Any

from inference.retrievers.retriever import Retriever
from indexing.enums.index_names import IndexName

class T5Retriever(Retriever):
    def __init__(self):
        self.index_name = IndexName.UWATERLOO_COURSES_INDEX_T5.value
        self.model_name = "sentence-transformers/sentence-t5-base"
        self.model = SentenceTransformer(self.model_name)
    
    def get_es_query(self, query: str, num_results: int = 5) -> dict[Any, Any]:
        embedding = self.model.encode(query)
        es_query = {
            "from": 0, 
            "size": num_results, 
            "_source": ["courseName", "courseDescription", "courseCode"], 
            "knn": {"field": "courseDescEncoding", "query_vector": embedding, "k": num_results, "num_candidates": 5000}}

        return es_query