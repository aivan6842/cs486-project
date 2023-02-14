from abc import ABC, abstractmethod
from elasticsearch import helpers

from shared.es.es_client import ES_CLIENT

class Indexer(ABC):
    
    def __init__(self, index_name: str, data: list):
        self.index_name = index_name
        self.data = data


    @abstractmethod
    def gen_data(self):
        return NotImplemented
    

    def index(self):
        helpers.bulk(ES_CLIENT, self.gen_data())
