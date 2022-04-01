#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'solve' below.
#
# The function is expected to return a value of type LONG INTEGER.
# The function accepts following parameters:
#  1. ar is of type INTEGER ARRAY.


def is_square(num):
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return True
    else:
        return False


def check_perfect_counts(subsets):
    # // setting to -1 since we want to exclude empty subset which will have product 1
    total = -1
    for subset in subsets:
        product = 1
        for num in subset:
            product *= num
            
        if is_square(product):
            total+= 1
    
    return total
    
    
def solve(arr):
    result = []
    result.append([])
    for num in arr:
        curr_size = len(result)
        for i in range(curr_size):
            subset = result[i].copy()
            subset.append(num)
            result.append(subset)
      
    #return result      
    return check_perfect_counts(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_count = int(input().strip())

    ar = []
    arItems = input().rstrip().split(" ")

    for i in range(ar_count):
        ar_item = int(arItems[i])
        ar.append(ar_item)

    outcome = solve(ar)

    fptr.write(str(outcome)  + '\n')

    fptr.close()

