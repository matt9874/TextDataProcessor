from abc import ABCMeta, abstractmethod

class TextDataProcessor:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def ProcessData(self):
        pass