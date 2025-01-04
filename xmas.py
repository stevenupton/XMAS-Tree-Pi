from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import time
import logging

logging.basicConfig(level=logging.DEBUG)

on = 10
off = 5
fade = 20

tree = LEDBoard(*range(3,28),pwm=True)
star = LEDBoard(2,pwm=True)
star.on()

tree.blink(on, off, fade, fade, None, True)

#while True:
#    if keyboard.read_key() == 'x':
#      print("X is pressed")
#      os.system("sudo shutdown now -h")
#      time.sleep(1)

 
pause()    

