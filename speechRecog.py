#!/usr/bin/env python3
import speech_recognition as sr
from speechResponse import speechResp
from myLog import logg
#================================================================================#
# Variables
rec = sr.Recognizer()
recWasInitailized = False
canYouRepeat = False

#================================================================================#
def setRepeat(boolVariable):
    logg('Set Repeat to: '+boolVariable, 'info')
    global canYouRepeat
    canYouRepeat = boolVariable

#================================================================================#
def speechRecInit():
    logg('Initalizing the speechRecognition.', 'info')
    global rec
    rec = sr.Recognizer()
    global recWasInitailized
    recWasInitailized = True

#================================================================================#
def speechRec():
    recognisedtext = ''

    if not recWasInitailized:
        speechRecInit()

    with sr.Microphone() as source:
        audio = rec.listen(source)

    try:
        recognisedtext = str(rec.recognize_google(audio))
        logg("You said: " + recognisedtext, 'info')
        if canYouRepeat:
            speechResp("You said: " + recognisedtext, 'en')

    except sr.UnknownValueError:
        message = "Could not understanded audio."
        #speechResp(message, 'en')
        logg(message, 'error')

    except sr.RequestError as e:
        message = "Could not request results; {0}".format(e)
        #speechResp(message, 'en')
        logg(message, 'error')

    return recognisedtext or ""