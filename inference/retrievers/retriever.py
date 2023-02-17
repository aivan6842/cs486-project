from abc import ABC, abstractmethod
from typing import Any

from shared.es.es_client import ES_CLIENT as es

class Retriever(ABC):
    
    @abstractmethod
    def get_es_query(self, query: str, num_results: int = 5) -> dict[Any, Any]:
        raise NotImplementedError

    def retrieve(self, query: str, num_results: int = 5) -> list[dict[str, str]]:
        body = self.get_es_query(query=query, num_results=num_results)
        return es.search(index=self.index_name, body=body)