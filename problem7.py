#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Smallest Multiple

def isPrime(number):

	for x in range(2,number):
		if (number % x) == 0:
			return False
	
	return True

def problem_7():
	i = 1
	currentNum = 2
	
	while i <= 10001:
		if isPrime(currentNum):
			i = i+1
		currentNum += 1
		print currentNum
	
	return currentNum-1		
	
if __name__ == '__main__':
	try:
		print problem_7()
	except (KeyboardInterupt):
		raise