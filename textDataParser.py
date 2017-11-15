from abc import ABCMeta, abstractmethod

class TextDataParser:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Parse(self):
        pass