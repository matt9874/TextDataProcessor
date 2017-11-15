from textDataFormatter import TextDataFormatter

class NewLineRemover(TextDataFormatter):
    def Format(self, text):
        return text.replace('\n', ' ')