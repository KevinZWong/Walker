# This program demonstrates the use of the PCA9685 PWM driver
# This is useful to effectively control multiple servos or motors
# In this example, there is a servo on channel 0 and channel 1
# The code also shows how you can control a motor (on channel 2)

# Libraries
import time
from adafruit_servokit import ServoKit

# Initialize ServoKit for the PWA board.
kit = ServoKit(channels=16)

# GPIO library not necessary if we only use the PWM driver
#import RPi.GPIO as GPIO

 
# GPIO Mode (BOARD / BCM)
#GPIO.setmode(GPIO.BOARD)


def servoAngle(channel, angle):
        kit.servo[channel].angle = angle
        print ('angle: {0} \t channel: {1}'.format(angle,channel))

def setAll(angle):
    servoAngle(0, angle)
    servoAngle(1, angle)
    servoAngle(2, angle)
    servoAngle(3, angle)



try:
    FSM1 = 0
    currentTime = time.time()
    while True:
        if (FSM1 == 0):
            if (time.time() - currentTime < 1):
                setAll(0)
            else:
                FSM1 = 1
                currentTime = time.time()
        elif (FSM1 == 1):
            if (time.time() - currentTime < 1):
                setAll(180)
            else:
                FSM1 = 0
                currentTime = time.time()


        




 
            
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
            pass
