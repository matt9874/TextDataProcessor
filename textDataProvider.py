from abc import ABCMeta, abstractmethod

class TextDataProvider:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def GetTextData(self):
        pass