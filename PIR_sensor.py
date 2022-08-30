
from gpiozero import MotionSensor
from gpiozero import LED
from signal import pause
from time import sleep



green_led = LED(17)
pir = MotionSensor(4)
green_led.off()


while True:
    pir.wait_for_motion()
    print("Motion Detected")
    green_led.on()
    pir.wait_for_no_motion()
    green_led.off()
    print("Motion Stopped")
    
    