#! /usr/bin/python

# Christian Sherland
# 2-24-13
# Project Euler - Largest palindrome product of two 3-digit numbers 

def is_palindrome(to_test):
    return to_test == to_test[::-1]

def problem_4():

    for n in reversed(xrange(10000, 998001)):
        if is_palindrome(str(n)):
            for factor_1 in reversed(xrange(1000)):
                for factor_2 in reversed(xrange(1000)):
                    if n == (factor_2 * factor_1):
                        return n

    return 255  # Return a sentinel value to indicate failure.

if __name__ == '__main__':      
    print problem_4()
