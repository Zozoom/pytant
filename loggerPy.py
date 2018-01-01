#!/usr/bin/env python
import os, errno
import time
import logging

#================================================================================#
# Variables
defaultMsg = ''
directory = 'logs/'
logFileName = 'tempLog_'+time.strftime('%Y_%m_%d')+'.log'
wasInit = False
#================================================================================#
# Get Actual Time in String
def getTimeInStr():
    return str(time.strftime('%Y/%m/%d  %H:%M:%S')) 
#================================================================================#
#Log Init
def log_init():
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    
    LOG_FILENAME = directory+logFileName
    logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
    logging.info('\n')
    logging.info(' ********* Starting at '+time.strftime('%Y/%m/%d  %H:%M:%S')+' *********')

    defaultMsg = getTimeInStr()+': Logger was inicialized.'   
    print (defaultMsg)
    logging.info(defaultMsg)
    global wasInit
    wasInit = True
    
#================================================================================#
#Logger
def logger(message,level):
    if(not wasInit):
        log_init()
    defaultMsg = getTimeInStr()+': '+level+' > '+message   
    print (defaultMsg)
    logging.info(defaultMsg)
 
 