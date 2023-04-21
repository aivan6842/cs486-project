from evaluation.metrics.metric import Metric

class Recall(Metric):
    #def evaluate(self, y: list, yhat: list):
    def evaluate(self,y:list,y_hat:list):
        sum=0
        for j in range(len(y)):
            yj=set(y[j])
            yhatj=set(y_hat[j])
            sum+=len(yj.intersection(yhatj))/len(yj)
        return sum/len(y)