#!/usr/bin/env python
import os
import time
import pyspeedtest
from emailPy import send_email
from loggerPy import logger

#================================================================================#
# Variables
global sleep, warnTemp

emailMsg = ''
defaultMsg = ''
lanIp = ''
wanIp = ''
sleep = 2
warnTemp = 45
maxWarnTemp = 60
#================================================================================#
# Return CPU temperature as a character string
def getCPUtemperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return(res.replace("temp=","").replace("'C\n",""))
#================================================================================#
# Get back my Lan adress
def getMyLanAdress():
    res = os.popen("hostname -I").readline()
    res = res.split(' ')
    lanIp = res[0]
    logger(lanIp,'INFO')
    return lanIp
#================================================================================#
# Get back my Wan adress
def getMyWanAdress():
    res = os.popen("hostname -I").readline()
    res = res.split(' ')
    wanIp = res[1]
    logger(wanIp,'INFO')
    return wanIp    
#================================================================================#
# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))
#================================================================================#
# Return the Ghz of the CPU
def getClock():
    clock = float(os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").readline())
    clock = clock/1000000
    return(str(clock))
#================================================================================#
# Network check
def getNetworkInfos():
    st = pyspeedtest.SpeedTest()
    
    defaultMsg = ' --- Checking Network --- '   
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')  
    
    defaultMsg = ' Ping: %d ms' % st.ping()
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')  
    
    defaultMsg = ' Download speed: %s' % pretty_speed(st.download())
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')  
    
    defaultMsg = ' Upload speed: %s' % pretty_speed(st.upload())
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')  
#================================================================================#
# Pretty writing of the Network Speed   
def pretty_speed(speed):
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.2f %s' % (speed, units[unit])
#================================================================================#
# Get Actual Time in String
def getTimeInStr():
    return str(time.strftime('%Y/%m/%d  %H:%M:%S'))
#================================================================================#
#Calculation Of The Temp
def calculationOfTheTemp():
    prevtemp = 0
    maxHighTemp = 0
    while True :    
        #Calculations
        temp1 = float(getCPUtemperature())
        CPU_usage = getCPUuse()
        CPU_clock = getClock()           
        #Temp decision 
        if(temp1 > maxHighTemp):
                maxHighTemp = temp1
        #Log message
        logmsg = time.strftime('%Y/%m/%d  %H:%M:%S')+": ActTemp: "+str(temp1)+" C"+" / HighTemp: "+str(maxHighTemp)+" C"+" Usage: "+str(CPU_usage)+" %"+ " Clock: "+str(CPU_clock)+" Ghz" 
        #Temp decision 
        if(abs(prevtemp-temp1) > 0.5): 
            logger(logmsg,'INFO') 
            #print (logmsg)
            print ("Temp-Diff:", round(abs(prevtemp-temp1),2))        
            time.sleep(sleep)        
            prevtemp = temp1            
        if(temp1 > warnTemp):
            emailMsg = '\nHello its too hot here!\n'+logmsg
            send_email('','RaspberryPi: HOT Warning!',emailMsg)
        if(temp1 > maxWarnTemp):
            emailMsg = '\nSorry too HOT so Iwill shuting down...\n'+logmsg
            send_email('','RaspberryPi: HOTEST! Shutingdown!',emailMsg)
            time.sleep(3) 
            #os.popen("shutdown -r now")
#================================================================================#
def main():	
    defaultMsg = ' Initializing Network Conections...'
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')   
    getNetworkInfos()
    lanIp = getMyLanAdress()
    wanIp = getMyWanAdress()
    
    defaultMsg = ' Sending Startup Email...'   
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')   	
    emailMsg = getTimeInStr()+'\n\nHi RaspberryPi is up n running...\n'+'Adress Lan: '+lanIp+'\nAdress Wan: '+wanIp+'\nWarn Temp is '+str(warnTemp)+' C'+'\nShutdown Temp is '+str(maxWarnTemp)+' C'
    send_email('','RaspberryPi: Welcome Up n Running',emailMsg)

    defaultMsg = ' Starting Temperature Monitoring...'   
    #print getTimeInStr() + defaultMsg
    logger(defaultMsg,'INFO')   	
    calculationOfTheTemp()
#================================================================================#
if __name__ == "__main__":
    main()