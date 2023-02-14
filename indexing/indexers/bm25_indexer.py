from indexing.indexers.indexer import Indexer

class BM25Indexer(Indexer):
    
    def gen_data(self):
        for item in self.data:
            yield {
                "_index": self.index_name,
                "_source": item
            }