import textFilesProvider as tfProv
import textFilesParser as tfParser
import textFilesOutputter as tfOutP

class TextFilesProcessor:
    def __init__(self):
        self.textFilesProvider=tfProv.TextFilesProvider()
        self.textFilesParser=tfParser.TextFilesParser()
        self.textFilesOutputter=tfOutP.TextFilesOutputter()
    def ProcessData(self):
        textFilesData = self.textFilesProvider.GetTextFilesData()
        parsedTextFilesData = self.textFilesParser.Parse(textFilesData)
        self.textFilesOutputter.Display(parsedTextFilesData)
        

