#!/bin/python3

# Our first python module

from gpiozero import Robot
import time

robby = Robot(left=(7,8), right=(9,10))

robby.backward()
time.sleep(20)
robby.stop()