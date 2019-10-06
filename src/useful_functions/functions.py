# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:11:32 2019

@author: Daniel
"""

import numpy as np
import pandas as pd
import nltk
from textblob import Word
nltk.download('wordnet')
from nltk.corpus import wordnet

# =============================================================================
# Função que irá ler todo o arquivo txt que contenha as palavras a serem estudas
# Retorna uma lista de palavras 
# =============================================================================

def getWords(path: str):
    f = open(path)
    for line in f:
    	words = line.split(',')
    	print(words)
    f.close()
    print('Documento fechado!')
    return words

# =============================================================================
# Função que retorna todos os sinônimos dada uma palavra
# Também apresenta: 
#    Todos os synsets dessa palavra
#    Classe gramatical da palavra
#    Exemplo de utilização da palavra
# =============================================================================

def getSynonyms(word: str):
    print('Getting Synonyms from ' + word)
    syn = list()
    
    print('List synsets for ' + word)
    for synset in wordnet.synsets(word):
        print('Synset found: '+ synset.definition())
        print('Part of Speech: ' + synset.pos())
        if len(synset.examples()) > 0:
            print('Example for this synset: ' + synset.examples()[0])
        else :
            print('There is no example for this synset')
        for lemma in synset.lemmas():
            print('Found synonym ' + lemma.name())
            syn.append(lemma.name())
    print('>>>>>>>>>>> End of function getSynonym <<<<<<<<<<<<')
    return syn

# =============================================================================
# Função que retorna todos os antônimos dada uma palavra
# Também apresenta: 
#    Todos os synsets dessa palavra
#    Classe gramatical do synset
#    Exemplo de utilização do synset
# =============================================================================

def getAntonyms(word: str):
    print('Getting Antonyms from ' + word)
    ant = list()
    
    print('List synsets for ' + word)
    for synset in wordnet.synsets(word):
        print('Synset found: '+ synset.definition())
        print('Part of Speech: ' + synset.pos())
        for lemma in synset.lemmas():
            if lemma.antonyms():
                for antonym in lemma.antonyms():
                    print('Found antonym ' + antonym.name())
                    ant.append(antonym.name())
            else :
                print('There is no antonym for this synset')
    print('>>>>>>>>>>> End of function getAntonym <<<<<<<<<<<<')
    return ant