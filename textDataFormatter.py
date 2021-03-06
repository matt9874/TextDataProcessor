from abc import ABCMeta, abstractmethod

class TextDataFormatter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Format(self):
        pass