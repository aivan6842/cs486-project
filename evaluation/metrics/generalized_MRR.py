from evaluation.metrics.metric import Metric

class GeneralizedMeanReciprocalRank(Metric):
    def evaluate(self,y:list,y_hat:list):
        sum=0
        #import pdb; pdb.set_trace()
        for j in range(len(y)):
            yj=set(y[j])
            #yhatj=set(y_hat[j])
            q=len(yj)
            first_match_index=0.0
            #if first_match_index==0.0:
            for i in range(q):
                if y_hat[j][i] in yj:
                    first_match_index= 1/(i+1)
                    break
            sum+=first_match_index
        return sum/len(y)