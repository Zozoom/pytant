#!/usr/bin/env python3
import time
import errno, os
import pygame
from gtts import gTTS
from myLog import logg

#================================================================================#
# Variables
directory = 'temp/'
speakTempFile = directory + 'temp.mp3'
speechWasInitailized = False

#================================================================================#
def folderIsExist(path):
    logg('Checking the folders...', 'info')
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            logg('In speechResp '+path+' directory was created!', 'info')
        except OSError as e:
            if e.errno != errno.EEXIST:
                logg('Something went wrong: '+e.message, 'error')
                raise
    else:
        logg('In speechResp '+path + ' directory already exist!', 'info')

#================================================================================#
def speechRespInit():
    logg('Initalizing the speechResp.', 'info')
    folderIsExist(directory)
    pygame.init()
    global speechWasInitailized
    speechWasInitailized = True

#================================================================================#
def speechResp(vcText,language):

    if not speechWasInitailized:
        speechRespInit()

    tts = gTTS(text=vcText, lang=language)
    tts.save(speakTempFile)

    pygame.mixer.music.load(speakTempFile)
    pygame.mixer.music.play(0)
    logg('Speeching: < '+vcText+' >', 'info')

    while pygame.mixer.music.get_busy() == True:
        time.sleep(1)
        #print ('Playin...')

    pygame.mixer.music.stop()
    #logg('Speeching: > Stopped <', 'info')

    #print ('Remove...')
    #os.remove(speakTempFile)
