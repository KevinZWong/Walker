# Libraries
import RPi.GPIO as GPIO
import time
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
# set GPIO Pins
GPIO_Servo = 7

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Servo, GPIO.OUT)



# Set PWM parameters
pwm_frequency = 50
duty_min = 2.5 * float(pwm_frequency) / 50.0
duty_max = 12.5 * float(pwm_frequency) / 50.0


# Set the duty cycle
def set_duty_cycle(angle):
    return ((duty_max - duty_min) * float(angle) / 180.0 + duty_min)

    
# Create a PWM instance
pwm_servo = GPIO.PWM(GPIO_Servo, pwm_frequency)



# Keep track of the state
FSM1State = 0
FSM1NextState = 0
angle = 0
pwm_servo.start(set_duty_cycle(angle))

# Keep track of the timing
FSM1LastTime = 0

print("Press CTRL+C to end the program.")

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
            # State 0: angle of 0 or on the way there
            if (FSM1State == 0):        

                if (currentTime - FSM1LastTime > 1):
                    angle = 45
                    pwm_servo.ChangeDutyCycle(set_duty_cycle(angle))
                    FSM1NextState = 1
                    print ("Move to 45 degrees")

                else:
                    FSM1NextState = 0

            # State 1: angle of 45 or on the way there
            elif (FSM1State == 1):      

                if (currentTime - FSM1LastTime > 1):
                    angle = 90
                    pwm_servo.ChangeDutyCycle(set_duty_cycle(angle))
                    FSM1NextState = 2
                    print ("Move to 90 degrees")

                else:
                    FSM1NextState = 1

            # State 2: angle of 90 or on the way there
            elif (FSM1State == 2):      

                if (currentTime - FSM1LastTime > 1):
                    angle = 135
                    pwm_servo.ChangeDutyCycle(set_duty_cycle(angle))
                    FSM1NextState = 3
                    print ("Move to 135 degrees")

                else:
                    FSM1NextState = 2

            # State 3: angle of 135 or on the way there
            elif (FSM1State == 3):      

                if (currentTime - FSM1LastTime > 1):
                    angle = 180
                    pwm_servo.ChangeDutyCycle(set_duty_cycle(angle))
                    FSM1NextState = 4
                    print ("Move to 180 degrees")

                else:
                    FSM1NextState = 3

            # State 4: angle of 180 or on the way there
            elif (FSM1State == 4):      

                if (currentTime - FSM1LastTime > 1):
                    angle = 0
                    pwm_servo.ChangeDutyCycle(set_duty_cycle(angle))
                    FSM1NextState = 0
                    print ("Move to 0 degrees")

                else:
                    FSM1NextState = 4
                    
            # State ??
            else:
                print("Error: unrecognized state for FSM1")
                noError = False   

            # If there is a state change, record the time    
            if (FSM1State != FSM1NextState):
                FSM1LastTime = currentTime
                
                                
        # Clean up GPIO if there was an error
        GPIO.cleanup()                


            
            
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
        GPIO.cleanup()                          # Release resource
