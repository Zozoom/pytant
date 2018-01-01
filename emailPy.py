#!/usr/bin/env python
import smtplib
import time
from loggerPy import logger
#================================================================================#
# Variables
emailMsg = ''
defaultMsg = ''
#================================================================================#
# Get Actual Time in String
def getTimeInStr():
    return str(time.strftime('%Y/%m/%d  %H:%M:%S')) 
#================================================================================#
#Log setup
def send_email(recipient, subject, body):

    defaultMsg = ' Initializing Email Sending...'   
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')   
    
    user = ''
    pwd = ''
    defaultRecipient = ''
    
    if(not recipient):
        recipient = defaultRecipient
    
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body +'\n\nRegards Raspi!\nFrom: '+FROM+'\nhttps://docs.resin.io/img/device/raspberry-pi3.svg'
    #print 'email body: '+ body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        defaultMsg = ' Connecting to smtp server...'   
        #print getTimeInStr() + defaultMsg
        logger(defaultMsg,'INFO')   
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
          
        defaultMsg = ' Successfully sent the mail.'   
        #print getTimeInStr() + defaultMsg
        logger(defaultMsg,'INFO')    
    except:  
        defaultMsg = ' Failed to send mail!'   
        #print getTimeInStr() + defaultMsg
        logger(defaultMsg,'ERROR') 
        
#================================================================================#  
def main():
    defaultMsg = ' Initializing Email Sending...'   
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO') 
    #send_email('kiss.zoltan.pti@gmail.com','RaspBerry Msg','Hi I am Raspi remember me ?')  
#================================================================================#
if __name__ == "__main__":
    main()