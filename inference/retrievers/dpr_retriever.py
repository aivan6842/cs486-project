from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer
from typing import Any
from torch.nn.functional import normalize
from inference.retrievers.retriever import Retriever
from indexing.enums.index_names import IndexName


class DPRRetriever(Retriever):
    def __init__(self):
        self.index_name = IndexName.UWATERLOO_COURSES_INDEX_DPR.value
        self.model_name = "facebook/dpr-question_encoder-single-nq-base"
        self.tokenizer = DPRQuestionEncoderTokenizer.from_pretrained(self.model_name)
        self.model = DPRQuestionEncoder.from_pretrained(self.model_name)
    
    def get_es_query(self, query: str, num_results: int = 5) -> dict[Any, Any]:
        input_ids = self.tokenizer(query, return_tensors="pt")["input_ids"]
        embedding = normalize(self.model(input_ids).pooler_output).tolist()[0]
        es_query = {
            "from": 0, 
            "size": num_results, 
            "_source": ["courseName", "courseDescription", "courseCode"], 
            "knn": {"field": "courseDescEncoding", "query_vector": embedding, "k": num_results, "num_candidates": 5000}}

        return es_query