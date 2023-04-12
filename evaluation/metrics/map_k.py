from evaluation.metrics.metric import Metric

class Mapk(Metric):
    def evaluate(self, y: list, yhat: list):
        return self.mapk(y=y, yhat=yhat, k=10)

    #Average precision at k
    def apk(self, y: list, yhat: list, k: int=0):
        #Dont need to check if lists are the same since reranker will take care if multimodel, single model wont make dups
        #Make sure k isnt greater than 5 as we only have top 5 results
        if k != 0:
            y, yhat = y[:k], yhat[:k]

        correct_predictions = 0
        running_sum = 0

        for i, yhat_item in enumerate(yhat):
            k = i+1

            if yhat_item in y:
                correct_predictions += 1
                running_sum += correct_predictions/k

        return running_sum/len(y)

    def mapk(self, y: list, yhat: list, k: int=0):
        apk_sum = 0
        for i in range(len(y)):
            apk_sum += self.apk(y[i], yhat[i])

        return apk_sum/len(y)