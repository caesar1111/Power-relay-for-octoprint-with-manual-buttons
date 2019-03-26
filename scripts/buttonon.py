#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO 2

while True:
    input_state = GPIO.input(2)
    if input_state == False:
        os.system("/home/pi/scripts/lighton.sh && /home/pi/scripts/poweron.sh")
        time.sleep(1)
	
        
