#!/usr/bin/env python3
import logging
import errno
import os
import time
from enum import Enum

#================================================================================#
# Variables
defaultMsg = ''
directory = 'logs/'
logName = ''
AppName = 'Pytant_app'
logWasInitailized = False

logger = logging.getLogger(AppName)

#================================================================================#
# Enums
class LogLevels(Enum):
    debug = 'debug'
    error = 'error'
    critical = 'critical'
    exception = 'exception'
    info = 'info'

#================================================================================#
# Get Actual Time in String
def logAppNameSetter(inAppName):
    global logger, AppName
    AppName = inAppName
    logger = logging.getLogger(AppName)
    initLogger()

#================================================================================#
# Get Actual Time in String
def getTimeAsStr():
    return str(time.strftime('%Y_%m_%d'))

#================================================================================#
def folderIsExist(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            print str(time.strftime('%Y:%m:%d %H:%M:%S'))+' - App:[myLog] - [INFO] > The '+path+' directory was created!'
        except OSError as e:
            if e.errno != errno.EEXIST:
                print str(time.strftime('%Y:%m:%d %H:%M:%S'))+' - App:[myLog] - [INFO] > The '+'Something went wrong: '+e.message
                raise
    else:
        print str(time.strftime('%Y:%m:%d %H:%M:%S'))+' - App:[myLog] - [INFO] > The '+path + ' directory already exist!'

#================================================================================#
def logg(logMsg,logLevel):

    if not logWasInitailized:
        initLogger()

    logLevel = logLevel.lower()

    if(logLevel == LogLevels.info):
        logger.info(logMsg)
    elif(logLevel == LogLevels.debug):
        logger.debug(logMsg)
    elif(logLevel == LogLevels.error):
        logger.error(logMsg)
    elif(logLevel == LogLevels.critical):
        logger.critical(logMsg)
    elif(logLevel == LogLevels.exception):
        logger.exception(logMsg)
    elif (logLevel == ''):
        print('* Your log level is empty please give a log level! - Note: This message wont be written!*')
        print('* You log is: ' + logMsg + logLevel + ' *')
    else:
        print('* There is no '+logLevel+' what you want! Choose another one. *')
        print('* You log is: ' + logMsg + logLevel + ' *')

#================================================================================#
def initLogger():

    folderIsExist(directory)

    logName = directory+'pytant_'+getTimeAsStr()+'.log'

    # create logger with 'spam_application'
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(logName)
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - App:[%(name)s] - [%(levelname)s] > %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info('\n\n**************************** LOG ['+AppName+'] ['+getTimeAsStr()+'] ****************************')

    global logWasInitailized
    logWasInitailized = True


#================================================================================#
if __name__ == "__main__":
    initLogger()