from collections import OrderedDict
#import nltk

class TextFilesParser:
    def Parse(self, textFiles):
        wordCounts = {}
#        wordDocuments={}
#        wordSentences={}
        for fileName in textFiles:
            with open( fileName, "r" ) as fileObject:
                for line in fileObject:
                    for word in line.split():
                        if (word in wordCounts.keys()):
                            wordCounts[word]=wordCounts[word]+1
                        else:
                            wordCounts[word]=1
        sortedWords=OrderedDict(sorted(wordCounts.items(), key=lambda t: -t[1]))
#        print sortedWords
        return sortedWords
        
        
        