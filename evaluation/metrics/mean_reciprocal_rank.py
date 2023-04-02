from evaluation.metrics.metric import Metric

class MeanReciprocalRank(Metric):
    def evaluate(self,y:list,y_hat:list):
        q=len(y)
        res=0
        for i in range(q):
            top=y[i][0]
            index=-1
            try :
                index=y_hat[i].index(top)+1
            except ValueError:
                index=-1
            reciprocal_rank=1/index if index != -1 else 0
            res+=reciprocal_rank
        
        return res/q