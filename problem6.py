#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Smallest Multiple

def problem_6a():
	cumSum1 = 0

	for y1 in range(1,101):
		cumSum1 += y1
		
	cumSum1 *= cumSum1
	return cumSum1
	
def problem_6b():
	cumSum2 = 0
	
	for y2 in range(1,101):
		cumSum2 += (y2*y2)
		
	return cumSum2

if __name__ == '__main__':
	print problem_6a() - problem_6b()
	