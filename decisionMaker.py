#!/usr/bin/env python3
import datetime
from myLog import logg
from speechRecog import speechRec
from speechResponse import speechResp
from random import randrange
import asistanCore
import synonymSearch
#================================================================================#
# Variables
goodBye = True
#================================================================================#
# Questioning list.
thankAskList = ["thanks","thank you"]
goodbyeAskList = ["goodbye","bye","that's all"]

myDictonary = {
    "what time is it":'It is ' + str(datetime.datetime.now().hour) + 'o clock and ' + str(datetime.datetime.now().minute) + ' minutes.',
    "what is the time":'It is ' + str(datetime.datetime.now().hour) + 'o clock and ' + str(datetime.datetime.now().minute) + ' minutes.',
    "what's the time":'It is ' + str(datetime.datetime.now().hour) + 'o clock and ' + str(datetime.datetime.now().minute) + ' minutes.',
    "help me out":"You can ask from me: my name, the time, ask help",
    "help":"You can ask from me: my name, the time, ask help",
    "help me":"You can ask from me: my name, the time, ask help",
    "what is your name": "My name is " + asistanCore.aiName,
    "what was your name": "My name was " + asistanCore.aiName,
    "what's your name": "I'm " + asistanCore.aiName
}

#================================================================================#
# Answering list.
welcomeAnswerList = ["You are welcome","No worries","No problem","Not at all","my pleasure","it's nothing"]

#================================================================================#
def decisions():
    global decisionIsDone
    decisionIsDone = False
    logg('decisionIsDone' + str(decisionIsDone), 'info')

    while not decisionIsDone:

        recognisedText = speechRec()

        logg('Searching decision for: ' + recognisedText, 'info')

        # /////////////////////////////////////////////////////////////////////////////
        # My Dictonary
        if recognisedText in myDictonary.keys():
            for key, value in myDictonary.items():
                if key == recognisedText:
                    speechResp(value, 'en')

        # /////////////////////////////////////////////////////////////////////////////
        # Thank you
        elif recognisedText in thankAskList:
            message = welcomeAnswerList[randrange(0, len(welcomeAnswerList))]
            speechResp(message, 'en')

        # /////////////////////////////////////////////////////////////////////////////
        # Good bye
        elif recognisedText in goodbyeAskList:
            speechResp('Have a nice day and Good Bye!', 'en')
            global goodBye
            goodBye = False
            break
        else:
            speechResp('Sorry I cannot understand what have you said. Could you repeat it?!', 'en')
            decisionIsDone = False

        decisionIsDone = True

    logg('decisionIsDone' + str(decisionIsDone), 'info')
    return decisionIsDone