# !/usr/bin/engv python3
'''
Approximating pi. 

Author: Zhipeng Xie

Credits: Based on code on p.78 Miller and Ranum text.
			'python.org' official document

Approximate pi using a Monte Carlo simulation.
'''
import math
import random
def isInCircle(x, y, r = 1):
	'''
(float or int, float or int, optional float or int) -> bool

Input the position and radius of a circle whose center is (0,0),
then determine if this position is in circle

>>> isInCircle(0, 0, 1)
    True
>>> isInCircle(.5, .5, 1)
    True
>>> isInCircle(1, 2, 1)
    False
	'''
	d = math.sqrt(pow(x,2) + pow(y,2))
	if d <= r:
		return True
	return False

def montePI(the_range):
	'''
(int) -> float

Input the range of iteration, return the approximation of PI
using the Monte Carlo algorithm

>>> montePi(100)
    3.2
>>> montePi(100000)
    3.141304
	'''
	result = 0.0
	for i in range(the_range):
		x = random.random()
		y = random.random()
		if isInCircle(x,y):
			result = result + 1
	return result*4/the_range

def showMontePi(times):
	'''
	(int) -> String

	Input the range of iteration, using the result of function montePi
	return Comparsion result.
	
	>>> showMontePi(100)
With 100 iterations (darts):
my approximate value for pi is:  3.120000000000000
math lib pi value is:  3.1415926535897931
This is a 0.687316 percent error.
	>>> showMontePi(1000)
With 1000 iterations (darts):
my approximate value for pi is:  3.208000000000000
math lib pi value is:  3.1415926535897931
This is a 2.113811 percent error.
	>>> showMontePi(10000)
With 10000 iterations (darts):
my approximate value for pi is:  3.156800000000000
math lib pi value is:  3.1415926535897931
This is a 0.484065 percent error.
	'''
	PI = montePI(times)
	difference = abs((PI - math.pi)/math.pi) * 100
	result = '''With %d iterations (darts):
my approximate value for pi is:  %.15f
math lib pi value is:  %.16f
This is a %f percent error.''' %(times,PI, math.pi, difference)
	return result

times = 10000
print(showMontePi(times))