import glob

class TextFilesProvider:
    def __init__(self):
        self.textFilesLocation="C:\\TextFilesInput"
    def GetTextFilesData(self):
        textFilesList = glob.glob(self.textFilesLocation+"./*.txt")
        print textFilesList
        return textFilesList
