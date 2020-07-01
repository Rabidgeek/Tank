import pygame, sys, time, os
import RPi.GPIO as GPIO

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.putenv('DISPLAY', ':0.0')
pygame.init()
pygame.joystick.init()
pygame.display.init()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pitchPin = 26
GPIO.setup(pitchPin, GPIO.OUT)
pitch = GPIO.PWM(pitchPin, 50)

travel = 0.5
positionY = 1
lastPosY = positionY
moveY = 0

def backline():
	print('\r', end=' ')

print("There are {} controller(s) available.".format(pygame.joystick.get_count()))
_joystick = pygame.joystick.Joystick(0)
_joystick.init()

print("initializing joystick:		 {}".format(_joystick.get_init()))
print("ID:				 {}".format(_joystick.get_id()))
print("Name:				 {}".format(_joystick.get_name()))
print("Number of Axes: 		 {}".format(_joystick.get_numaxes()))
print("Number of Ballz:		 {}".format(_joystick.get_numballs()))
print("Number of Buttons:		 {}".format(_joystick.get_numbuttons()))
print("Number of Hats:			 {}".format(_joystick.get_numhats()))

print("Right Vertical			Right Horizontal		Current Position")

axes = _joystick.get_numaxes()

pitch.start(positionY)

while True:
	pygame.event.pump()
	yawAxis = (pygame.joystick.Joystick(0).get_axis(2))
	pitchAxis = (pygame.joystick.Joystick(0).get_axis(3))

	if pitchAxis > 0:	# Move joystick down
		moveY = pitchAxis * ( travel / 5 )
		positionY = positionY + -moveY
		lastPosY = positionY
		if positionY < 1.5:
			positionY = 1.5
		if positionY > 12.5:
			positionY = 12.5
		pygame.event.pump()

	elif pitchAxis < 0:	# Move joystick up
		moveY =  pitchAxis * ( travel / 5 ) 
		positionY = positionY - moveY
		lastPosY = positionY
		if positionY > 12:
			positionY = 12
		if positionY < 1.5:
			positionY = 1.5
		pygame.event.pump()

	elif pitchAxis == 0:
		positionY = lastPosY

	print("{:0.1f}				{:0.1f}				{}".format(pitchAxis, yawAxis, positionY), end=" ")
	backline()
	backline()
	pitch.ChangeDutyCycle(positionY)
	time.sleep(0.1)
