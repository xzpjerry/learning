# ! /usr/bin/engv python3
'''
  Art_show, Assignment 3, CIS 210
  
  Authors:  Zhipeng Xie
  
  Credits: 'python.org' document

  Using turtle to draw a simple shape(The house)
'''
from turtle import *
def turn_and_go(diration, angle_and_distance):
	'''
	(tuple, tuple) ->  None

	Inputing diration tuple and angle_and_distance tuple,
	it can reconize both diration and distance needed to forward,
	then draw the result(A House)

	Nothing returned
	>>> turn_and_go (('straight'), ((0,100),) ) 
	This will draw a straight line from (0,0) point left-toward 100 pixels
	>>> turn_and_go (('straight','left'), ((0,100),(45,100)) ) 
	This will draw a straight line from (0,0) point left-toward 100 pixels
	and then draw a line toward its 45 degree 100 pixels

	'''
	a = 0
	jj = 0
	for dira in diration:
		if dira == 'left':
			left(angle_and_distance[a][jj])
			forward(angle_and_distance[a][jj+1])
		elif dira == 'right':
			right(angle_and_distance[a][jj])
			forward(angle_and_distance[a][jj+1])
		else:
			forward(angle_and_distance[a][jj+1])
		a = a + 1
	return None

def art_show():
	'''
	() -> None

	Using to execute drawing process
	first set the starting point to appropriate position
	then set appropriate color and background color
	then loading data(guide_book & parameter_book) that needed to draw the object(The House)
	calling the turn_and_go function to do the specific job
	In the parameter_book tuple, first parameter is the angle, the second one is distance.

	Nothing returned

	>>> artshow()
	will draw a House
	'''
	bgcolor("#13d876")
	screensize(1280,720)
	penup()
	setpos(-330,-250)
	color("#605b28", "#b2a423")
	pendown()
	begin_fill()
	guide_book = ('straight','left','left','right','right','right','left','left')
	parameter_book = ((0,50), (90,200), (90,50),(135,410), (90,410),(135,50),(90,200), (90,200))
	turn_and_go(guide_book, parameter_book)
	end_fill()
	done()
	return None

art_show()
