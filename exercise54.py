# This is where Exercise 5.4 goes
# Name: Ceceilia Allwein


import math 


def is_triangle():
	'''If you have three sticks, you may or may not be able to 
	make a triangle. 

	FERMATS LAST THEOREM says that if the length of any one 
	stick (a, b, or c) is greater than the sum of the other two 
	(a+b, a+c, or b+c) you can't make a triangle. 

	This function determines if it's possible to make a triangle 
	with three user-defined side lengths.'''

	print "How long is each side of the triangle?"
	print "Please enter three numbers, and press enter between each."
	a = int(raw_input())
	b = int(raw_input())
	c = int(raw_input())
	if a > (b+c) or b > (a+c) or c > (a+b):
		print "Sorry, no dice."
	elif a == (b+c) or b == (a+c) or c == (a+b): 
		print "Your triangle is degenerate."
	else: 
		print "You made a triangle. Such a smart baby!"

is_triangle ()



def signal_to_noise_ratio():
	''' Computes the signal to noise ratio 
	in decibels based on user input.''' 

	print "What is the signal power? Please input a number between 1 and 10."
	signal_power = int(raw_input())
	print "what is the noise_power? Please input a number between 1 and 10."
	noise_power = int (raw_input())
	ratio = signal_power / noise_power
	decibels = 10 * math.log10(ratio)
	if signal_power > 10 or noise_power > 10: 
		print "Please try again."
	else: 
		print decibels

signal_to_noise_ratio()
