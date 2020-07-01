from pysabertooth import Sabertooth
import pygame, time, sys, os

motor = Sabertooth("/dev/serial0", baudrate=9600, address=128)

os.environ["SDL_VIDEODRIVER"] = "dummy"	#initialize dummy video screen
os.putenv('DISPLAY', ':0.0')		#set display, pygame requires this

pygame.init()				#initialize pygame
pygame.joystick.init()			#initialzie joystick
pygame.display.init()			#initialize display

while True:
	pygame.event.pump()
	

	time.sleep(0.1)
