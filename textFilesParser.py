import wordDataMapper as wdm
#import nltk
#nltk.download('punkt')
from nltk import tokenize

class TextFilesParser:
    def __init__(self):
        self.wordDataMapper=wdm.WordDataMapper()
    def Parse(self, textFiles):
        wordCounts = {}
        wordDocuments={}
        wordSentences={}
        for fileName in textFiles:
            with open( fileName, "r" ) as fileObject:
                rawText=fileObject.read()
                sentences = tokenize.sent_tokenize(rawText) 
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
    
        