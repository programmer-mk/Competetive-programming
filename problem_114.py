#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'square_cut' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. A is of type INTEGER.
#  2. B is of type INTEGER.


def square_cut_recursive(A,B):
    if A == B:
        result = 1
    elif A > B:
        result = 1 + square_cut_recursive(A-B,B)
    else:
        result = 1 + square_cut_recursive(A,B-A) 
    
    return result
    
def square_cut(A,B):
    if A <= 0 or B <= 0:
        return -1
    else:
        return square_cut_recursive(A, B)

if __name__ == '__main__':
    A = int(input().strip())
    B = int(input().strip())
    outcome = square_cut(A, B)
    print(f'Min number of squares: {outcome}')

