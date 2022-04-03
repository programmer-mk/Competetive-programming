#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'solve' below.
#
# The function is expected to return a value of type INTEGER ARRAY.
# The function accepts following parameters:
#  1. n is of type INTEGER.

"""
   array: 1 2 2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 8

   One hidden test fails??
"""

def solve(n):
    result = [1] * (n**2+n)
    result[1] = 2
    write_index = 1
    for i in range(1, n):
        for k in range(0, result[i]):
            result[write_index] = i+1
            write_index+= 1

    return result[:n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    n = int(input().strip())
    outcome = solve(n)

    for i in range(len(outcome)):
        fptr.write(str(outcome[i]))
        if i < len(outcome)-1:
            fptr.write(" ")
    fptr.write("\n")

    fptr.close()

