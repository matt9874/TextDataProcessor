from abc import ABCMeta, abstractmethod

class TextDataProcessorFactory:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def CreateProcessor(self):
        pass
    
    @abstractmethod
    def CreateProvider(self):
        pass
    
    @abstractmethod
    def CreateParser(self):
        pass
    
    @abstractmethod
    def CreateOutputter(self):
        pass