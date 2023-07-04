#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

switch = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN)

while True:
    print('Switch status = ', GPIO.input(switch))

GPIO.cleanup()