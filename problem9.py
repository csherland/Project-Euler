#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Special Pythagorean Triplet

import math

def problem_9():

        productOfTriplets = 0;

        triplets = [0,0,0]
        
        for m in range(1,1000):
                for n in range(1,1000):
                        if m + n + math.sqrt(m*m + n*n) == 1000:
                                triplets[0] = m
                                triplets[1] = n
                                triplets[2] = math.sqrt(m*m + n*n)              
                                return triplets


if __name__ == '__main__':
        x =  problem_9()
        print x[0]
        print x[1]
        print x[2]
        
        print x[0]*x[0] + x[1]*x[1]
        print x[2]*x[2]
        
        print x[0]*x[1]*x[2]
