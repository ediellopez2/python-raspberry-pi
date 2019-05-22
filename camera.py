# Tutorial can be found at 'projects.raspberrypi.org'
from picamera import PiCamera
from time import sleep
import datetime
camera = PiCamera()

camera.start_preview()
for i in range(5):
    sleep(2)
    currentTime = str(datetime.datetime.now())
    print("Taking a picture now!")
    camera.capture('/home/pi/Desktop/security/' + currentTime + '.jpg')
camera.stop_preview()
