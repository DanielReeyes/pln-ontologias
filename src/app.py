#http://www.nltk.org/howto/wordnet.html

from useful_functions.functions import *
PATH = 'data/words.txt'

words = getWords(PATH)
listSynonym = getSynonyms(words[0])
listAntonym = getAntonyms(words[0])
