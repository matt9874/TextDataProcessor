import tabulate as tab

class TextFilesOutputter:
    def __init__(self):
        self.numResults=5
    def Display(self,textDataRecords):
        textDataRecords.sort(key=lambda x: x.count, reverse=True)
        formattedData=[]
        numWords=len(textDataRecords)
        if (type(self.numResults) is int and self.numResults>=0 and self.numResults<numWords):
            outputSize=self.numResults
        for i in range(0,outputSize):
            wordData=textDataRecords[i]
            formattedData.append([wordData.word, wordData.count, ', '.join(wordData.containingDocuments), '\n\n'.join(wordData.containingSentences)])
        print tab.tabulate(formattedData, headers=['Word', 'Count', 'Documents', 'Sentences containing the word'], tablefmt='grid')
