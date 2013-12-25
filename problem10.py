#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Special Pythagorean Triplet

import math

def isPrime(number):

	if (number <= 3):
		return True

	for x in range(2,int(math.ceil(math.sqrt(number)))+1):
		if (number % x) == 0:
			return False
	
	return True

def problem_10():

	cumSum = 0

	for i in range(2, 2000001):
		if isPrime(i):
			cumSum += i
	
	return cumSum

if __name__ == '__main__':
	print problem_10()