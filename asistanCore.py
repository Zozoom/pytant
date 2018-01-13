# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from myLog import logg
from speechResponse import speechResp
from speechRecog import speechRec
from random import randrange
import decisionMaker
import configparser

#================================================================================#
# Variables
aiName = ''
# Lists
qaBackList = ''

# ================================================================================#
def setConfigs():
    global aiName, qaBackList
    config = configparser.ConfigParser()
    config.read('all.config')
    qaBackList = config['Answers']['caller'].split(",")
    aiName = config['BASIC']['aiName']

# ================================================================================#
def main():

    # Starting section
    logg('Start the Asistant python...', 'info')
    speechResp("Hello! My name is "+aiName+". What a wonderful day!", 'en')

    # What can i do ? - section
    while decisionMaker.goodBye:
        logg("Waiting for user command...[Step 1]", 'info')
        word = speechRec()
        if aiName in word:
            message = qaBackList[randrange(0, len(qaBackList))]
            speechResp(message, 'en')
            logg("Waiting for user command...[Step 2]", 'info')
            if decisionMaker.decisions():
                message = 'Something else what can I do for you ?'
                speechResp(message, 'en')
                logg("Waiting for user command...[Step 3]", 'info')
                decisionMaker.decisions()
        else:
            logg("Skipped...", 'info')

# ================================================================================#
if __name__ == "__main__":
    setConfigs()
    main()