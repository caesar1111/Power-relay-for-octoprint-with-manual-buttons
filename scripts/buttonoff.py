#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO 3

while True:
    input_state = GPIO.input(3)
    if input_state == False:
        os.system("/home/pi/scripts/lightoff.sh && /home/pi/scripts/poweroff.sh")
        time.sleep(1)
	
        
