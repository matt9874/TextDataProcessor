import wordDataMapper as wdm
import textDataFormatter as tdf
#import nltk
#nltk.download('punkt')
from nltk import tokenize

class TextFilesParser:
    def __init__(self):
        self.wordDataMapper=wdm.WordDataMapper()
        self.textFormatter=tdf.TextDataFormatter()
        
    def Parse(self, textFiles):
#        formattedTextFiles=map(self.RemoveLineEndings,textFiles)
        wordCounts = {}
        wordDocuments={}
        wordSentences={}
        for fileName in textFiles:
            with open( fileName, "r" ) as fileObject:
                rawText=fileObject.read()
                formattedRawText=self.textFormatter.Format(rawText)
                sentences = tokenize.sent_tokenize(formattedRawText) 
                for sentence in sentences:
                    words = tokenize.word_tokenize(sentence)
                    for word in words:
                        if (word in wordCounts.keys()):
                            wordCounts[word]=wordCounts[word]+1
                            wordSentences[word].add(sentence)
                            wordDocuments[word].add(fileName)
                        else:
                            wordCounts[word]=1
                            wordSentences[word]={sentence}
                            wordDocuments[word]={fileName}
        
        output = self.wordDataMapper.MapWordData(wordCounts, wordDocuments, wordSentences)
        
        return output