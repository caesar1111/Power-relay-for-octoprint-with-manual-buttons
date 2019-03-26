#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO 4

while True:
    input_state = GPIO.input(4)
    if input_state == False:
	os.system("sudo shutdown now")
        time.sleep(1)

