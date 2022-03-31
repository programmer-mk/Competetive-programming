#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'rearrange' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. S is of type STRING.


def rearrange(nums):
    occurencies = {}
    for num in nums:
        if occurencies.get(num):
            occurencies[num] += 1
        else:
            occurencies[num] = 1
    
    temp = 0        
    for idx, key in enumerate(occurencies):
        if idx == 0:
            temp = occurencies[key]
        else:
            temp = abs(temp - occurencies[key])
            
    if temp > 1:
        return 0
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    S = input()

    outcome = rearrange(S)
    fptr.write(str(outcome)  + '\n')
    fptr.close()

