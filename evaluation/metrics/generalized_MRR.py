from evaluation.metrics.metric import Metric

class GeneralizedMeanReciprocalRank(Metric):
    def evaluate(self,y:list,y_hat:list):
        q=len(y)
        res=0
        for i in range(q):
            s=0
            index_of_first_relevant=-1
            for j in range(10):
                if index_of_first_relevant==-1:
                    index_of_first_relevant=j
                reciprocal_rank=index_of_first_relevant if index_of_first_relevant != -1 else 0
                s+=reciprocal_rank
            s=s/10
            res+=s
        
        return res/q