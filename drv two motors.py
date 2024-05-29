import time
import concurrent.futures
import RPi.GPIO as GPIO

# Next 3 lines for development local library testing import
# Comment out in production release and change RpiMotorLib.A4988Nema to A4988Nema
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
#from RpiMotorLib import A4988Nema

# Production installed library import
from RpiMotorLib import RpiMotorLib

# To Test motor stop, put push button to VCC on GPIO 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO pins
# Microstep Resolution M0-M1-M2 -> GPIO Pin
# Note: you can Pass in (-1,-1,-1) if you wish to hardwire Ms-X to logic and
# Save GPIO pins.

# Motor 1
en_1 = 22
direction_1 = 23  # Direction -> GPIO Pin
step_1  = 24      # Step -> GPIO Pin

# Motor 2
en_2 = 17
direction_2 = 19  # Direction -> GPIO Pin
step_2  = 13      # Step -> GPIO Pin

# Declare two named instance of class, one for each motor
mymotortestOne = RpiMotorLib.A4988Nema(direction_1, step_1, (21,21,21), "DRV8825")
mymotortestTwo = RpiMotorLib.A4988Nema(direction_2, step_2, (21,21,21), "DRV8825")
GPIO.setup(en_1, GPIO.OUT)
GPIO.setup(en_2, GPIO.OUT) 
def main():
    """main function loop"""

    # ====== tests for two motor DRV8835 ====
    # motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        GPIO.output(en_1, GPIO.LOW)
        GPIO.output(en_2, GPIO.LOW)
        f1 = executor.submit(mymotortestOne.motor_go, True, "Full" , 800, .005, False, .05)
        f2 = executor.submit(mymotortestTwo.motor_go, False, "Full" , 1600, .005, False, .05)



# ===================MAIN===============================

if __name__ == '__main__':

    print("START")
    main()
    GPIO.cleanup() # Optional
    print("END")
    exit()

# =====================END===============================
