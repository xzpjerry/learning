# !/usr/bin/engv python3
'''
  My_sqrt.  Assignment 2, CIS 210
  
  Authors:  Zhipeng Xie
  
  Credits: 'python.org' document

  Input number and iteration times, out put its square root,
  comparing the result with built-in sqrt function
'''
import math
def brain(target, times):
	'''
	(float or int, int) -> float

	return calculated square root result based
	on inputed taget number and iteration times
	Nothing is printed
	'''
	temp = 1
	for i in range(times):
		temp = 0.5 * (temp + target/temp)
	result = temp
	return result

def mysqrt(num_need_sqrted, num_of_times):
	'''
	(float or int, int) -> string

	Print the square root of target number based
	on the inputed number and iteration times,
	using the brain function.
	None Value is returned.

	>>> mysqrt(25, 5)
    5.00002317825
    >>> mysqrt(25, 10)
    5.0
    >>> mysqrt(100, 10)
    10.0
    >>> mysqrt(625, 10)
    25.0
    >>> mysqrt(10000, 8)
    101.202183654
    >>> mysqrt(10000, 10)
    100.000000255
    >>> mysqrt(10000, 11)
    100.0
	'''
	if(isinstance(num_need_sqrted,(int,float))):
		if(isinstance(num_of_times,(int))):
			print(round(brain(num_need_sqrted,num_of_times),15))
		else:
			raise TypeError('Bad num_of_times')
	else:
		raise TypeError('Bad num_need_sqrted')

def sqrt_compare(num_need_sqrted, num_of_times):
	'''
	(float or int, int) -> string

	Print the comparing result of my_sqrt & built-in sqrt functions
	based on the inputed number and iteration times
	in charge of determining if the parameters are legal

	>>> sqrt_compae(10000, 8)
	For  10000 using 8 iterations:
	mysqrt value is:  100.0
	math lib sqrt value is:  101.202183654
	This is a 0.01 percent error.
	
	>>> sqrt_compare('sss','sss')
	File "mysqrt.py", line 94, in <module>
    sqrt_compare(a,b)
    File "mysqrt.py", line 88, in sqrt_compare
    raise TypeError('Bad num_need_sqrted')
	TypeError: Bad num_need_sqrted

	>>> sqrt_compare(25, 5)
	For  25 using 5 iterations:
	mysqrt value is:  5.0
	math lib sqrt value is:  5.00002317825
	This is a 0.00 percent error.
	'''
	if(isinstance(num_need_sqrted,(int,float))):
		if(isinstance(num_of_times,(int))):
			sqrt_result = math.sqrt(num_need_sqrted)
			my_result = round(brain(num_need_sqrted,num_of_times),15)
			print('''For  %s using %s iterations:
mysqrt value is:  %s
math lib sqrt value is:  %s
This is a %.2f percent error.  ''' % (num_need_sqrted, num_of_times, sqrt_result, my_result, abs((sqrt_result - my_result)/sqrt_result)))
		else:
			raise TypeError('Bad num_of_times')
	else:
		raise TypeError('Bad num_need_sqrted')



a = 25
b = 5
sqrt_compare(a,b)
