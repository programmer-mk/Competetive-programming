#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'solve' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. a is of type INTEGER ARRAY.
#  2. b is of type INTEGER ARRAY.
#  3. p is of type INTEGER.
#  4. q is of type INTEGER.


"""
    A lot of tests fails on Glider platform. Not sure what's missing, founding longest common subsequence should be enough here.
"""

def lcs(a, b, idx1, idx2):
    if idx1 == len(a) or idx2 == len(b):
        return 0
    elif a[idx1] == b[idx2]:
        return 1 + lcs(a, b, idx1+1, idx2+1)
    else:
        return max(lcs(a, b, idx1+1, idx2), lcs(a, b, idx1, idx2+1))

def solve(a,b,p,q):
    base = lcs(a, b, 0, 0)
    return (len(a)-base)*p + (len(b)-base)*q


if __name__ == '__main__':
    a = [1, 2, 3, 4,5,2,3,1,42,3,2,1,23,1]
    b = [1, 1, 2, 3, 4, 2, 1,23,3,2,1]
    print(solve(a, b,7,8))