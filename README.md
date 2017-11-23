# TextDataProcessor
#
# Written in Python 2.7 
#
# If you are on a Windows machine, please create a new folder in the C drive called TextFilesInput.
# Then place text files in this folder
#
# Alternatively, you can modify the textFilesLocation variable in textFilesProvider.py (from "C:\\TextFilesInput") to the location of the text files.
#
# Run main.py to analyze the text files.
#
# NLTK:
# This application is dependant on the NLTK library. Some parts of the NLTK may need to be downloaded for it to run so lines 2-3 in wordValidator.py and lines 4-5 in textFilesParser.py may need to be uncommented on the first run of this application.
#
# Variables that affect the results:
# Presently the instance variable at line 8 of tabulatedWordCountOutputter.py called numResults is set to 10. This variable controls the maximum number of words returned in the results. If this is changed to a value that is not a non-negative integer, then there will be no maximum number of words returned.
# Presently the instance variable at line 9 of wordValidator.py called removeStopWordsFromResults is set to True. This variable controls whether or not stopwords (specifically the set of NLTK's english stopwords) are removed from the results. This can be changed to false to include stopwords in the results.
