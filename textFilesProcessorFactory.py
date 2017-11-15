from textDataProcessorFactory import TextDataProcessorFactory
from textFilesProcessor import TextFilesProcessor
from textFilesProvider import TextFilesProvider
from textFilesParser import TextFilesParser
from tabulatedWordCountOutputter import TabulatedWordCountOutputter
from newLineRemover import NewLineRemover
from wordDataMapper import WordDataMapper

class TextFilesProcessorFactory(TextDataProcessorFactory):
    @staticmethod
    def CreateProcessor():
        return TextFilesProcessor(TextFilesProcessorFactory.CreateProvider(), TextFilesProcessorFactory.CreateParser(), TextFilesProcessorFactory.CreateOutputter())
    
    @staticmethod
    def CreateProvider():
        return TextFilesProvider()
    
    @staticmethod
    def CreateParser():
        return TextFilesParser(NewLineRemover(),WordDataMapper())
    
    @staticmethod
    def CreateOutputter():
        return TabulatedWordCountOutputter()