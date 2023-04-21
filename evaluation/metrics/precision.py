from evaluation.metrics.metric import Metric

class Precision(Metric):
    def evaluate(self, y:list ,y_hat:list):
    #def evaluate(self, y: list, yhat: list):
        sum=0
        for j in range(len(y)):
            yj=set(y[j])
            yhatj=set(y_hat[j])
            sum+=len(yj.intersection(yhatj))/len(yj)
        return sum