from evaluation.metrics.metric import Metric

class Precision(Metric):
    def evaluate(self, y: list, yhat: list):
        y=set(y)
        yhat=set(yhat)
        return len(y.intersection(yhat))/len(yhat)