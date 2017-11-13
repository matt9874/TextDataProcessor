
#import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords

class WordValidator:
    def __init__(self):
        self.stopWords=set(stopwords.words('english'))
    def Validate(self, word):
        return not word in self.stopWords