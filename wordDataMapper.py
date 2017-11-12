import wordInfo as wi

class WordDataMapper:
    def MapWordData(self, wordCounts, wordDocuments, wordSentences):
        outputList=[]
        for key, value in wordCounts.iteritems():
            wordInfo=wi.WordInfo(key,value,wordDocuments[key],wordSentences[key])
            outputList.append(wordInfo)
        return outputList