from abc import ABC, abstractmethod

class Metric(ABC):
    
    @abstractmethod
    def evaluate(self,y:list,y_hat:list):
        raise NotImplementedError
    


