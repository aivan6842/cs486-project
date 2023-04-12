from evaluation.metrics.metric import Metric

class GeneralizedMeanReciprocalRank(Metric):
    def evaluate(self,y:list,y_hat:list):
        q=len(y)
        for i in range(q):
            if y_hat[i] in y:
                return 1/(i+1)
        return 0