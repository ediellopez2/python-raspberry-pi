# Controlling an LED with a button
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
GPIO.setwarnings(False)

Button = 12     # GPIO 12
LedPin = 21     # GPIO 21

GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)# Set Up Button to GPIO12
GPIO.setup(LedPin, GPIO.OUT)                         # Set Up LED to GPIO21

if __name__ == '__main__':  # Program starts here
    try:
        print("Everything is good to go, chief!")
        while True:
             # print(str(GPIO.input(Button)))

             # button_state holds 0 when the button is pressed. 1 otherwise.
             button_state = GPIO.input(Button)
             if button_state == False:
                 GPIO.output(LedPin, True)
                 print('Button Pressed...')
                 time.sleep(1.0)
             else:
                 GPIO.output(LedPin, False)
    except KeyboardInterrupt:   # 'ctrl+c' to stop
        GPIO.cleanup()
