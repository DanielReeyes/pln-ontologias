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

TARGET_PATH = 'data/results.txt'

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
        print('Part of Speech: ' + getPartOfSpeechTranslated(synset.pos()))
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
        print('Part of Speech: ' + getPartOfSpeechTranslated(synset.pos()))
        for lemma in synset.lemmas():
            if lemma.antonyms():
                for antonym in lemma.antonyms():
                    print('Found antonym ' + antonym.name())
                    ant.append(antonym.name())
            else :
                print('There is no antonym for this synset')
    print('>>>>>>>>>>> End of function getAntonym <<<<<<<<<<<<')
    return ant

# =============================================================================
# Função que retorna a classe gramatical por extenso e traduzida dada uma palavra
# =============================================================================

def getPartOfSpeechTranslated(partOfSpeech: str):
    if (partOfSpeech == 'n'):
        return 'SUBSTANTIVO'
    elif (partOfSpeech == 'a'):
        return 'ADJETIVO'
    elif (partOfSpeech == 's'):
        return 'ADJETIVO SATELITE'
    elif (partOfSpeech == 'r'):
        return 'ADVERBIO'
    elif (partOfSpeech == 'v'):
        return 'VERBO'

# =============================================================================
# Função que salva as informações 
# Modo de escrita é append
# Passado por parâmetro
#   - Caminho do arquivo destino
#   - Conteúdo a ser salvo
# =============================================================================
def saveResultsInFile(target_path: str, result: str):
    f = open(target_path, 'a')
    f.writelines(result)
    f.write('\n')
    f.close()

# =============================================================================
# Função que limpa as informações do arquivo de resultados
# # Passado por parâmetro
#   - Caminho do arquivo de resultados
# =============================================================================
def cleanResultsFile(target_path: str):
    open(target_path, 'w').close()

# =============================================================================
# Função que captura as informações de synset e sinonimos e exemplos
# Passado por parâmetro
#   - Palavra a ser pesquisada
# =============================================================================
def writeSynonyms(word: str):
    saveResultsInFile(TARGET_PATH, '>>> Getting Synonyms from ' + word)
    
    saveResultsInFile(TARGET_PATH, '>>> List synsets for ' + word)
    if len(wordnet.synsets(word)) > 0:
        for synset in wordnet.synsets(word):
            saveResultsInFile(TARGET_PATH, '>>>>>> Synset found: '+ synset.definition())
            saveResultsInFile(TARGET_PATH, '>>>>>>>>> Part of Speech: ' + getPartOfSpeechTranslated(synset.pos()))
            if len(synset.examples()) > 0:
                saveResultsInFile(TARGET_PATH, '>>>>>>>>> Example for this synset: ' + synset.examples()[0])
            else :
                saveResultsInFile(TARGET_PATH, '>>>>>>>>> There is no example for this synset')
            for lemma in synset.lemmas():
                saveResultsInFile(TARGET_PATH, '>>>>>>>>> Found synonym ' + lemma.name())
    else:
        saveResultsInFile(TARGET_PATH, 'There is no synset for this word')
    saveResultsInFile(TARGET_PATH, '>>>>>>>>>>> End of function getSynonym from '+str(word)+' <<<<<<<<<<<< \n')

# =============================================================================
# Função que captura as informações de synset e antônimos e exemplos
# Passado por parâmetro
#   - Palavra a ser pesquisada
# =============================================================================
def writeAntonyms(word: str):
    saveResultsInFile(TARGET_PATH, '>>> Getting Antonyms from ' + word)
    
    saveResultsInFile(TARGET_PATH, '>>> List synsets for ' + word)
    if len(wordnet.synsets(word)) > 0:
        for synset in wordnet.synsets(word):
            saveResultsInFile(TARGET_PATH, '>>>>>> Synset found: '+ synset.definition())
            saveResultsInFile(TARGET_PATH, '>>>>>>>>> Part of Speech: ' + getPartOfSpeechTranslated(synset.pos()))
            for lemma in synset.lemmas():
                if lemma.antonyms():
                    for antonym in lemma.antonyms():
                        saveResultsInFile(TARGET_PATH, '>>>>>>>>> Found antonym ' + antonym.name())
                else :
                    saveResultsInFile(TARGET_PATH, 'There is no antonym for this synset')
    saveResultsInFile(TARGET_PATH, 'There is no synset for this word')
    saveResultsInFile(TARGET_PATH, '>>>>>>>>>>> End of function getAntonym <<<<<<<<<<<< \n')