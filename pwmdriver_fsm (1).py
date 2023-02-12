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


print("Press CTRL+C to end the program.")


# Keep track of the state
FSM1State = 0
FSM1NextState = 0
angle = 0
channel = 0
kit.servo[channel].angle = angle
print ('angle: {0} \t channel: {1}'.format(angle,channel))


# Keep track of the timing
FSM1LastTime = 0


# Main program 
try:
        
    noError = True
    while noError:

        # Check the current time
        currentTime = time.time()

        # Update the state
        FSM1State = FSM1NextState


        # Check the state transitions for FSM 1
        # This is a Mealy FSM
        # State 0: angle of 0 on channel 0 or on the way there
        if (FSM1State == 0):        

            if (currentTime - FSM1LastTime > 1):
                angle = 45
                channel = 0
                kit.servo[channel].angle = angle
                print ('angle: {0} \t channel: {1}'.format(angle,channel))
                # If using a motor on channel 2
                # speed = 50
                # channel = 2
                # kit.continuous_servo[channel].throttle = speed
                # print ('speed: {0} \t channel: {1}'.format(speed,channel))
                FSM1NextState = 1
            else:
                FSM1NextState = 0

        # State 1: angle of 45 on channel 0 or on the way there
        elif (FSM1State == 1):      

            if (currentTime - FSM1LastTime > 1):
                angle = 90
                channel = 1
                kit.servo[channel].angle = angle
                print ('angle: {0} \t channel: {1}'.format(angle,channel))
                # If using a motor on channel 2
                # speed = 100
                # channel = 2
                # kit.continuous_servo[channel].throttle = speed  
                # print ('speed: {0} \t channel: {1}'.format(speed,channel))
                FSM1NextState = 2
            else:
                FSM1NextState = 1

        # State 2: angle of 90 on channel 1 or on the way there
        elif (FSM1State == 2):      


            
            if (currentTime - FSM1LastTime > 1):
                angle = 135
                channel = 0
                kit.servo[channel].angle = angle
                print ('angle: {0} \t channel: {1}'.format(angle,channel))
                FSM1NextState = 3
            else:
                FSM1NextState = 2

        # State 3: angle of 135 on channel 0 or on the way there
        elif (FSM1State == 3):      

            if (currentTime - FSM1LastTime > 1):
                angle = 180
                channel = 1
                kit.servo[channel].angle = angle
                print ('angle: {0} \t channel: {1}'.format(angle,channel))
                FSM1NextState = 4
            else:
                FSM1NextState = 3

        # State 4: angle of 180  on channel 1 or on the way there
        elif (FSM1State == 4):      

            if (currentTime - FSM1LastTime > 1):
                angle = 0
                channel = 0
                kit.servo[channel].angle = angle
                print ('angle: {0} \t channel: {1}'.format(angle,channel))
                FSM1NextState = 0

            else:
                FSM1NextState = 4
                
        # State ??
        else:
            print("Error: unrecognized state for FSM1")
            
        # If there is a state change, record the time    
        if (FSM1State != FSM1NextState):
            FSM1LastTime = currentTime
 
            
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
        pass
