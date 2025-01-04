import RPi.GPIO as GPIO
import time
import logging
import random
from random import randint
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

# GPIO outputs in order of LED numbers 
LEDS = [4,15,13,21,25,8,5,10,16,17,27,26,24,9,12,6,20,19,14,18,11,7,23,22]

#Total number of LEDs
TOTAL= len(LEDS)

#Star LED Number
STAR = 2

# Variable used if not in December
PULSE = 0
DECREASE = 0

# Number of loops before when changing the lights
loop_rotations = 50


# Set all GIOPs and PWMs
def setup():
    global pwm
    global starPWM
    pwm = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for x in range(0,TOTAL):
      GPIO.setup(LEDS[x], GPIO.OUT)
      pwm[x] = GPIO.PWM(LEDS[x], 50)
      pwm[x].start(1)

    #setup the star  
    GPIO.setup(STAR, GPIO.OUT)
    starPWM = GPIO.PWM(STAR, 50)
    starPWM.start(100)
    
# Used in December and limit to 25 after Christmas Day
def dayofdec():
  x = datetime.today().day
  if x > 25:
    x = 25
  return(x)

# function to set the LEDs
# leds - range of LEDs to turn on 1-24
# day - day of the month max is 25 (xmas day makes the star twinkle)
# lights - lights to turn on .. max is 24 
def setLEDs(leds, day, lights):
  
  #loop around for number of loop_rotations (50 * 0.2) == 10 seconds
  for i in range(0, loop_rotations):
      
    # Start from 1st day with 1 LED and build up to 25
    
    for x in range(0,lights):
     rand = randint(25,100)
     leds[x].start(1)
     leds[x].ChangeDutyCycle(rand)

    #if day is xmas day, then make the start twinkle
    if day == 25:
      rand = randint(25,100)
      starPWM.start(1)
      starPWM.ChangeDutyCycle(rand)
          
    time.sleep(0.2)
    stopLights()

# function to turn out all the lights
def stopLights():
  for x in range(0,TOTAL):
    pwm[x].stop()
  
  
setup()
stopLights()

while True:
    # Get month
    month = datetime.today().month
    day = dayofdec()

    #12 days of christmas.. show light all lights for the twelve days of christmas 25th -> 5th Jan
    if month == 1 and day <= 5 :
      day = 25
      month = 12
    
    lights = day
    if day == 25 :
      lights = 24
    
  
    # If Month is December start build Christmas tree
    if month == 12:
        leds = random.sample(pwm, lights)
        setLEDs(leds, day, lights)
        
    else:
    
      starPWM.ChangeDutyCycle(PULSE)
      time.sleep(0.1)
      # Decrease or increase pulse value
      if DECREASE == 0:
        PULSE += 5
      else:
        PULSE -= 5
      # If max value change direction
      if PULSE == 100:
        DECREASE = 1
      # If min value change direction
      if PULSE == 0:
        DECREASE = 0


            
    

