from textDataProvider import TextDataProvider
import glob

class TextFilesProvider(TextDataProvider):
    def __init__(self):
        self.textFilesLocation="C:\\TextFilesInput"
    def GetTextData(self):
        textFilesList = glob.glob(self.textFilesLocation+"./*.txt")
        return textFilesList
