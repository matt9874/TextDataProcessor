from textDataOutputter import TextDataOutputter

import tabulate as tab
import textwrap as tw

class TabulatedWordCountOutputter(TextDataOutputter):
    def __init__(self):
        self.numResults=10
    def Display(self,textDataRecords):
        textDataRecords.sort(key=lambda x: x.count, reverse=True)
        formattedData=[]
        numWords=len(textDataRecords)
        if (type(self.numResults) is int and self.numResults>=0 and self.numResults<numWords):
            outputSize=self.numResults
        for i in range(0,outputSize):
            wordData=textDataRecords[i]
            formattedData.append([wordData.word, wordData.count, self.FormatDocumentsTableCellText(wordData.containingDocuments, 40), self.FormatSentencesTableCellText(wordData.containingSentences, 40)])
        print tab.tabulate(formattedData, headers=['Word', 'Count', 'Documents', 'Sentences containing the word'], tablefmt='grid')
    
    def FormatSentencesTableCellText(self, sentencesList, columnWidth):
        sentencesListWithLineEndings=["\n".join(tw.wrap(sentence, columnWidth)) for sentence in sentencesList]
        return "\n\n".join(sentencesListWithLineEndings)
    
    def FormatDocumentsTableCellText(self, documentsList, columnWidth):
        return "\n".join(tw.wrap(', '.join(documentsList), columnWidth))
