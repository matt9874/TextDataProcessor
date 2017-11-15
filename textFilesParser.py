from textDataParser import TextDataParser
from wordValidator import WordValidator

#import nltk
#nltk.download('punkt')

from nltk import tokenize
from nltk.tokenize import RegexpTokenizer

class TextFilesParser(TextDataParser):
    def __init__(self, textDataFormatter, textResultsMapper):
        self.textResultsMapper=textResultsMapper
        self.textFormatter=textDataFormatter
        self.wordValidator=WordValidator()
        
    def Parse(self, textFiles):
        wordCounts = {}
        wordDocuments={}
        wordSentences={}
        
        wordTokenizer=RegexpTokenizer(r'\w+')
        
        for fileName in textFiles:
            with open( fileName, "r" ) as fileObject:
                rawText=fileObject.read()
                formattedRawText=self.textFormatter.Format(rawText)
                sentences = tokenize.sent_tokenize(formattedRawText.decode('utf-8')) 
                for sentence in sentences:
                    words = wordTokenizer.tokenize(sentence)
                    for word in words:
                        if (self.wordValidator.Validate(word.lower())):
                            if (word in wordCounts.keys()):
                                wordCounts[word]=wordCounts[word]+1
                                wordSentences[word].add(sentence)
                                wordDocuments[word].add(fileName)
                            else:
                                wordCounts[word]=1
                                wordSentences[word]={sentence}
                                wordDocuments[word]={fileName}
        
        output = self.textResultsMapper.MapTextResults(wordCounts, wordDocuments, wordSentences)
        
        return output