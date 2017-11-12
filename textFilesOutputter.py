import tabulate as tab

class TextFilesOutputter:
    def Display(self,parsedData):
        formattedData=[]
        numWords=len(parsedData)
        for i in range(0,numWords):
            wordData=parsedData[i]
            formattedData.append([wordData[0], wordData[1], ', '.join(wordData[2]), ', '.join(wordData[3])])
        print tab.tabulate(formattedData, headers=['Word', 'Count', 'Documents', 'Sentences containing the word'], tablefmt='orgtbl')
