# ============== Super Simple Security Camera =================
# =============================================================
# ITEMS YOU'LL NEED:
#   A. A camera
#   B. raspberry pi
#   C. PIR Motion Sensor
#   D. relay module
#   E. active buzzer
# =============================================================

import RPi.GPIO as GPIO
GPIO.cleanup()
import time
from time import sleep
from picamera import PiCamera
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motionSensor = 26
activeBuzzer = 13
camera = PiCamera()

GPIO.setup(motionSensor, GPIO.IN) 	 #PIR Motion Sensor
GPIO.setup(activeBuzzer, GPIO.OUT)  	 #Set activeBuzzer's mode is output
GPIO.output(activeBuzzer, False)

if __name__=="__main__":
    try:
        print("Initializing .... System is Warming Up!")
        time.sleep(3)
        print("System is ready to go!")
        while True:
            #print(GPIO.input(motionSensor))
            if GPIO.input(motionSensor):
                currentTime = str(datetime.datetime.now())
                print("Movement has been detected! Contacting local authorities now.")
                camera.start_preview()
                camera.capture('/home/pi/Desktop/security/' + currentTime + '.jpg')
                camera.stop_preview()
                GPIO.output(activeBuzzer, True)
                time.sleep(5)
                GPIO.output(activeBuzzer, False)
                # time.sleep(5)
                print("PIR Motion Sensor is ready again.")
                #time.sleep(2)
        #GPIO.setup(motionSensor, GPIO.IN)
    except KeyboardInterrupt:
        GPIO.output(activeBuzzer, GPIO.LOW)
        GPIO.cleanup()
