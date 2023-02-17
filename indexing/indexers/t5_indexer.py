from indexing.indexers.indexer import Indexer
from sentence_transformers import SentenceTransformer

class T5Indexer(Indexer):
    def __init__(self, index_name: str, data: list):
        super().__init__(index_name, data)
        self.encoder_name = "sentence-transformers/sentence-t5-base"
        self.encoder = SentenceTransformer(self.encoder_name)

    def gen_data(self):
        for item in self.data:
            encoding = self.encoder.encode(item["courseDescription"])
            item["courseDescEncoding"] = encoding
            yield {
                "_index": self.index_name,
                "_source": item
            }
            