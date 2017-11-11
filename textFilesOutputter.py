import tabulate as tab

class TextFilesOutputter:
    def Display(self,parsedData):
#        for key,value in parsedData.items():
        print tab.tabulate(parsedData.items(), headers=['Word', 'Count'], tablefmt='orgtbl')
