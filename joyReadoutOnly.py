import pygame, sys, time, os

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.putenv('DISPLAY', ':0.0')
pygame.init()
pygame.joystick.init()
pygame.display.init()

def backline():
	print('\r', end='')

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

print("Right Vertical			Right Horizontal")

axes = _joystick.get_numaxes()

while True:
	pygame.event.pump()
	yaw = (pygame.joystick.Joystick(0).get_axis(2))
	pitch = (pygame.joystick.Joystick(0).get_axis(3))

	print("{:0.2f}				{:0.2f}".format(pitch, yaw), end="")
	backline()
	time.sleep(0.1)

print(" ")
print(" ")

