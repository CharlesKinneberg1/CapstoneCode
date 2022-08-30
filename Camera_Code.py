
import subprocess
import datetime
import sys
import time

i=0

subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -SO "+str(i)+"pic.jpg",shell=True)
print('PIC CAPTURED')
        
# get the date and time, set the date and time as a filename
currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")

