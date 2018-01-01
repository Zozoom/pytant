#!/usr/bin/python
import os
import errno
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
            print ('Created !')
        except OSError as e:
            if e.errno != errno.EEXIST:
                print ('Error !'+e.errno)
                raise
    else:
        print ('Already exist !')

#================================================================================#
def VoiceNplay(vcText,language):
    
    tts = gTTS(text=vcText, lang=language)
    filename = directory+'temp.mp3'
    tts.save(filename)
    
    pygame.init()
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)
    print (vcText)

    while pygame.mixer.music.get_busy() == True:
        time.sleep(1)
        print ('Playin...')
    
    print ('Stopped and remove...')
    os.remove(filename)

#================================================================================#
def main():
    print ('Temp folder is exist ?')
    folderIsExist()

    print ('The Speaking stuf is initalizing...')
    VoiceNplay('How do ya do today ?','en')
    VoiceNplay('What was the weather like ?','en')
    VoiceNplay('Te meg ki vagy ?','hu')
    
#================================================================================#
if __name__ == "__main__":
    main()