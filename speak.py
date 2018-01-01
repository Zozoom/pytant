#!/usr/bin/env python
import errno
import os, stat
import time
from gtts import gTTS
import pygame
#================================================================================#
# Variables
defaultMsg = ''
directory = 'temp/'
#================================================================================#
def folderIsExist():
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
#================================================================================#
def VoiceNplay(vcText,language):
    
    tts = gTTS(text=vcText, lang=language)
    filename = directory+'temp.mp3'
    tts.save(filename)
    pygame.init()
    pygame.mixer.music.load(filename)
    
    pygame.mixer.music.play(0)
    print(vcText)

    while pygame.mixer.music.get_busy() == True:
        time.sleep(1)
        print ('Playin...')

    pygame.mixer.music.stop()

    print ('Stopped and remove...')
    #os.remove(filename) #remove temperory file

#================================================================================#
def main():
    print ('The Speaking stuf is initalizing...')
    VoiceNplay('How do ya do today ?','en')
    VoiceNplay('What was the weather like ?','en')
    VoiceNplay('Te meg ki vagy ?','hu')
    VoiceNplay('Az anyad magyarul is tudok...','hu')
    
#================================================================================#
if __name__ == "__main__":
    main()