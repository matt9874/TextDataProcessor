from abc import ABCMeta, abstractmethod

class TextDataOutputter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Display(self):
        pass