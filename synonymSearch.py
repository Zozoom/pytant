# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from nltk.corpus import wordnet
from myLog import logg
from speechRecog import speechRec
from speechResponse import speechResp

#================================================================================#
def getSynonyms(word):
    synonyms = []

    #speechResp("What synonyms would you like to know?", 'en')

    #word = speechRec()

    logg('Getting synonyms for: ' + word, 'info')

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name().encode("utf-8"))

    result = str(', '.join(e for e in set(synonyms)))

    #speechResp('The synonyms are: '+result, 'en')

    return result

# ================================================================================#
def getAntonyms(word):
    antonyms = []

    #speechResp("What antonyms would you like to know?", 'en')

    #word = speechRec()

    logg('Getting antonyms for: ' + word, 'info')

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name().encode("utf-8"))

    result = str(', '.join(e for e in set(antonyms)))

    #speechResp('The antonyms are: ' + result, 'en')

    return result

# ================================================================================#
def main():

    while True:
        inputText = raw_input("What synonyms would you like to know? \nAnsw: ")
        print '\nSynonyms:'
        print getSynonyms(inputText)

# ================================================================================#
if __name__ == "__main__":
    main()