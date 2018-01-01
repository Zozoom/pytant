#!/usr/bin/python
import os
import errno
from loggerPy import logger

#================================================================================#
def fileIsExist(fileName,pathDirectory):

    defaultMsg = 'Checking file is existing...'
    logger(defaultMsg, 'INFO')

    concatDirectory = pathDirectory+fileName

    if not os.path.exists(concatDirectory):
        try:
            os.makedirs(concatDirectory)
            defaultMsg = 'File ['+concatDirectory+'] is created!'
            logger(defaultMsg, 'INFO')
        except OSError as e:
            if e.errno != errno.EEXIST:
                defaultMsg = 'Something went wrong: '+e.errno
                logger(defaultMsg, 'ERROR')
                raise
    else:
        defaultMsg ='File [' + concatDirectory + '] is already exist!'
        logger(defaultMsg, 'INFO')

#================================================================================#
def folderIsExist(pathDirectory):

    defaultMsg = 'Checking folder is existing...'
    logger(defaultMsg, 'INFO')

    concatDirectory = pathDirectory

    if not os.path.exists(concatDirectory):
        try:
            os.makedirs(concatDirectory)
            defaultMsg = 'Folder ['+concatDirectory+'] is created!'
            logger(defaultMsg, 'INFO')
        except OSError as e:
            if e.errno != errno.EEXIST:
                defaultMsg = 'Something went wrong: '+e.errno
                logger(defaultMsg, 'ERROR')
                raise
    else:
        defaultMsg ='Folder [' + concatDirectory + '] is already exist!'
        logger(defaultMsg, 'INFO')
