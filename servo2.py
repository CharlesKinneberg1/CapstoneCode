
from piservo import Servo
import time

servo = Servo(12)

while True:
    servo.write(30)
    time.sleep(3)
    servo.write(90)
    time.sleep(3)
