from textFilesProcessor import TextFilesProcessor
from textFilesProvider import TextFilesProvider
from textFilesParser import TextFilesParser
from textFilesOutputter import TabulatedWordCountOutputter
from newLineRemover import NewLineRemover
from wordDataMapper import WordDataMapper

textDataProcessor=TextFilesProcessor(TextFilesProvider(), TextFilesParser(NewLineRemover(), WordDataMapper()), TabulatedWordCountOutputter())
textDataProcessor.ProcessData()
