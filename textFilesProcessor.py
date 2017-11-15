from textDataProcessor import TextDataProcessor

class TextFilesProcessor(TextDataProcessor):
    def __init__(self, textFilesProvider, textFilesParser, textFilesOutputter):
        self.textDataProvider=textFilesProvider
        self.textDataParser=textFilesParser
        self.textDataOutputter=textFilesOutputter
    def ProcessData(self):
        textFilesData = self.textDataProvider.GetTextData()
        parsedTextFilesData = self.textDataParser.Parse(textFilesData)
        self.textDataOutputter.Display(parsedTextFilesData)
        

