from indexing.indexers.indexer import Indexer
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
from torch.nn.functional import normalize 

class DPRIndexer(Indexer):
    def __init__(self, index_name: str, data: list):
        super().__init__(index_name, data)
        self.model_name = "facebook/dpr-ctx_encoder-single-nq-base"
        self.tokenizer = DPRContextEncoderTokenizer.from_pretrained(self.model_name)
        self.encoder = DPRContextEncoder.from_pretrained(self.model_name)

    def gen_data(self):
        for item in self.data:
            input_ids = self.tokenizer(item["courseDescription"], return_tensors="pt")["input_ids"]
            encoding = normalize(self.encoder(input_ids).pooler_output).tolist()[0]
            item["courseDescEncoding"] = encoding
            yield {
                "_index": self.index_name,
                "_source": item
            }
            