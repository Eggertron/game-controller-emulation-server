#!/bin/python

import time
import pyvjoy

print("============== Test Begin ==============")

MAX_VJOY = 32767
SLEEP_SECONDS = 5

j = pyvjoy.VJoyDevice(1)

def reset_all(j):
  print("== Resting Joystick ==")
  j.reset()
  j.reset_buttons()
  j.reset_povs()
  j.update()

def play_function(j,X,Y,Z,XRot):
  j.data.wAxisX = int(X * self.MAX_VJOY)
  j.data.wAxisY = int(Y * self.MAX_VJOY)
  j.data.wAxisZ = int(Z * self.MAX_VJOY)
  j.data.wAxisXRot = int(XRot * self.MAX_VJOY)
  j.update()

reset_all(j)
time.sleep(SLEEP_SECONDS)

print("== Test X axis and wait ==")

j.data.wAxisX = int(MAX_VJOY)
j.update()
time.sleep(SLEEP_SECONDS)

print("== Test Y axis and wait ==")
j.data.wAxisY = int(MAX_VJOY)
j.update()
time.sleep(SLEEP_SECONDS)

print("== Test Z axis and wait ==")
j.data.wAxisZ = int(MAX_VJOY)
j.update()
time.sleep(SLEEP_SECONDS)

reset_all(j)
