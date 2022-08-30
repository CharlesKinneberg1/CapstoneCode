# Camera 
import subprocess
import datetime
import sys
import time

# PIR Sensor 
from gpiozero import MotionSensor
from gpiozero import LED
from signal import pause
from time import sleep

# Servo motor
from piservo import Servo

# Files for Tensorflow model 
MODEL_FILENAME = 'model.pb'
LABELS_FILENAME = 'labels.txt'

# PIR sensor setup
pir = MotionSensor(4)

# Camera counter variable
i = 0

#servo setup
servo = Servo(12)


# Functions ###############################
def capture():
    global i
    i = i + 1
    # Captures image 
    subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -SO "+str(i)+"pic.jpg",shell=True)
    print('PIC CAPTURED')
    # get the date and time, set the date and time as a filename
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")


def servoControl():
    servo.start()
    servo.write(30)
    time.sleep(1)
    servo.write(90)
    time.sleep(1)
    
    #servo.min()
    #sleep(2)
    #servo.max()
    #sleep(2)
    #servo.mid()
    #sleep(2)
    

## Loop #############################
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    capture()
    
    sleep(1)
    servoControl()

    pir.wait_for_no_motion()
    print("Motion Stopped")
    servo.stop()
    
     
    
    

    
    