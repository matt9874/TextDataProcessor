import tabulate as tab

class TextFilesOutputter:
    def Display(self,textDataRecords):
        formattedData=[]
        numWords=len(textDataRecords)
        for i in range(0,numWords):
            wordData=textDataRecords[i]
            formattedData.append([wordData.word, wordData.count, ', '.join(wordData.containingDocuments), ', '.join(wordData.containingSentences)])
        print tab.tabulate(formattedData, headers=['Word', 'Count', 'Documents', 'Sentences containing the word'], tablefmt='orgtbl')
