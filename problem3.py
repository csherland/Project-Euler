#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Largest Prime Factor

largestFactor = 600851475143
currentDivisor = 2

while currentDivisor < largestFactor:
    if ((largestFactor % currentDivisor) == 0):
        largestFactor /= currentDivisor
        currentDivisor = 2
    else:
        currentDivisor += 1

print largestFactor
