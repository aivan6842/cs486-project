from evaluation.metrics.metric import Metric

class Recall(Metric):
    def evaluate(self, y: list, yhat: list):
        y=set(y)
        yhat=set(yhat)
        return len(y.intersection(yhat))/len(y)