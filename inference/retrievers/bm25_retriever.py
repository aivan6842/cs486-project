from typing import Any

from inference.retrievers.retriever import Retriever
from indexing.enums.index_names import IndexName

class BM25Retriever(Retriever):
    def __init__(self):
        self.index_name = IndexName.UWATERLOO_COURSES_INDEX.value   
    
    def get_es_query(self, query: str, num_results: int = 10) -> dict[Any, Any]:
        es_query = {"from": 0, "size": num_results, "query": {"match": {"courseDescription": query}}}
        return es_query