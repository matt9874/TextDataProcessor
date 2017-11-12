class WordValidator:
    def __init__(self):
        self.disallowedWords=set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    def Validate(self, word):
        return not word in self.disallowedWords