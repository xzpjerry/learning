# !/usr/bin/engv python3

from turtle import * 
import random
import math


def left_or_right():
	seed = random.randrange(0,2,1)
	if seed == 0:
		return False
	else:
		return True

def drawing():
	#canvas = Screen()
	#canvas.setworldcoordinates(-2,-2,2,2)
	penup()
	setpos(-100,-100)
	pendown()
	num_line = random.randrange(0,101,2)
	for i in range(num_line):
		angle = random.randrange(0,361,1)
		distance = random.randrange(0,101,1)
		if left_or_right:
			left(angle)
		else:
			right(angle)
		forward(distance)

drawing()
		

