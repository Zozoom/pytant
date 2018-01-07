#!/usr/bin/env python3
from myLog import logg
from speechResponse import speechResp
from speechRecog import speechRec
from random import randrange
import decisionMaker

#================================================================================#
# Variables
aiName = 'Lena'

# Lists
qaBackList = ["I'm listening.","What can I do for you?","Can I help you?","Did you call me?","Did you say my name?","Did you say something?"]

# ================================================================================#
def main():

    # Starting section
    logg('Start the Asistant python...', 'info')
    speechResp("Hello! My name is "+aiName+". What a wonderful day!", 'en')

    # What can i do ? - section
    while decisionMaker.goodBye:
        message = qaBackList[randrange(0, len(qaBackList))]
        speechResp(message, 'en')
        logg("Waiting for user command...", 'info')
        decisionMaker.decisions(speechRec())

# ================================================================================#
if __name__ == "__main__":
    main()