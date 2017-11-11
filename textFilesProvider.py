import glob

class TextFilesProvider:
    def __init__(self):
        self.textFilesLocation="C:\\TextFilesInput"
    def GetTextFilesData(self):
        textFilesList = glob.glob(self.textFilesLocation+"./*.txt")
        print textFilesList
        return textFilesList
#        for fileName in textFilesList:
#            data_list = open( fileName, "r" ).readlines()
#            fout.write(data_list[17])
#            fout.writelines(data_list[44:])
