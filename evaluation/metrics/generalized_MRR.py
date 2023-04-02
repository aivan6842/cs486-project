from evaluation.metrics.metric import Metric

class GeneralizedMeanReciprocalRank(Metric):
    def evaluate(self,y:list,y_hat:list):
        q=len(y)
        res=0
        for i in range(q):
            s=0
            for j in range(10):
                top=y[i][j]
                index=-1
                try :
                    index=y_hat[i].index(top)+1
                except ValueError:
                    index=-1
                reciprocal_rank=1/index if index != -1 else 0
                s+=reciprocal_rank
            s=s/10
            res+=s
        
        return res/q