import pygame, sys, time, os
import RPi.GPIO as GPIO

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.putenv('DISPLAY', ':0.0')
pygame.init()
pygame.joystick.init()
pygame.display.init()

def backline():
	print('\r', end='')

pitchPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pitchPin, GPIO.OUT)

pitch = GPIO.PWM(pitchPin, 50)

travel = .5
position = 1
move = 0

pAxis = pygame.joystick.Joystick(0)
pAxis.init()

while True:
	pygame.event.pump()
#	yaw = (pygame.joystick.Joystick(0).get_axis(2))
	pitch = (pAxis.get_axis(3))

	if pitch > 0:
		move = pitch * (travel / 1023)
		position = position - move
		if position < 1:
			position = 1
	if pitch < 0:
		move = travel - (pitch * (travel / 1020))
		position = position + move
		if position > 12:
			position = 12

pitch.ChangeDutyPosition(position)

time.sleep(0.1)
