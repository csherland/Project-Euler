#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Smallest Multiple

def evenlyDivisibleBy(number):

	for x in range(11,20):
		if (number % x) == 0:
			continue
		else:
			return False
		
	return True
	
def problem_5():
	i = 1

	while i < 999999999:
		if evenlyDivisibleBy(i):
			return i
			
		i += 1
		
	
	return 555
	
if __name__ == '__main__':
	print problem_5()
	