#http://www.nltk.org/howto/wordnet.html

from useful_functions.functions import *
PATH = 'data/words.txt'
TARGET_PATH = 'data/results.txt'

cleanResultsFile(TARGET_PATH)
words = getWords(PATH)

for word in words:
    listSynonym = getSynonyms(word)
    listAntonym = getAntonyms(word)
    writeSynonyms(word)
    writeAntonyms(word)