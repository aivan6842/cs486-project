from abc import ABC, abstractmethod

class Reranker(ABC):
    
    @abstractmethod
    def rerank(self, data: list[tuple[str, str, str]], query: str) -> list[tuple[str, str, str]]:
        raise NotImplementedError