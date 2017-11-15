from abc import ABCMeta, abstractmethod

class TextResultsMapper:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def MapTextResults(self):
        pass