import math
import subprocess
import sys
import time


def shutdown (t):
    t*=60
    cmd = 'shutdown /s /f /d up:125:1 /t 300'
    p = subprocess.Popen(cmd, shell=True)

def timer (t):
    t = int(t)
    hour = math.floor(t/60)
    min = t - 60*hour
    sec = 0
    c=':'
    #sec = 30
    #min = 5
    #hour = 0

    #count up clock
    while hour+min+sec!=0:
        for y in range(59):                                                 #hours
            for x in range (59):                                            #min
                if sec!=0: sec-=1
                sec1 = ('%02.f' % sec)                                      #format
                min1 = ('%02.f' % min)
                hour1= ('%02.f' % hour)
                sys.stdout.write('\r'+str(hour1)+c+str(min1)+c+str(sec1))   #clear and write
                time.sleep(1)
            sec = 0
            sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + '00')  #ensure proper timing and display
            time.sleep(1)
            if min!=0: min-=1
        min = 0
        sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + '00')      #ensure proper timing and display
        time.sleep(1)
        if hour!=0: hour-=1


#main
in_time = input("Time (min): ")
#shutdown(in_time)
timer(in_time)