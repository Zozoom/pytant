#!/usr/bin/python
import time
import logging
from isFileExist import folderIsExist

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

    folderIsExist(directory)
    
    log_filename = directory+logFileName
    logging.basicConfig(filename=log_filename,level=logging.INFO)
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

    defaultMsg = getTimeInStr()+': ['+level+'] > '+message+' <'
    print (defaultMsg)
    logging.info(defaultMsg)