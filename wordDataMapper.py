from textResultsMapper import TextResultsMapper
from wordInfo import WordInfo

class WordDataMapper(TextResultsMapper):
    def MapTextResults(self, wordCounts, wordDocuments, wordSentences):
        outputList=[]
        for key, value in wordCounts.iteritems():
            wordInfo=WordInfo(key,value,wordDocuments[key],wordSentences[key])
            outputList.append(wordInfo)
        return outputList