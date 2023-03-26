from inference.rerankers.reranker import Reranker
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class BERTReranker(Reranker):

    def __init__(self) -> None:
        self.model_name="bert-base-uncased"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
   
    def rerank(self, data: list[tuple[str, str, str]], query: str) -> list[tuple[str, str, str]]:
        scores = []
        for doc in data:
            course_description=doc[2]
            input_text = query + " [SEP] " + course_description
            input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
            logits = self.model(input_ids).logits
            probs = torch.softmax(logits, dim=1)
            score = probs[0][1].item()
            scores.append(score)

        scored_data = [(data[i], scores[i]) for i in range(len(scores))]
        sorted_data = sorted(scored_data, key = lambda x : x[1], reverse=True)
        sorted_data = [item[0] for item in sorted_data]
        return sorted_data
