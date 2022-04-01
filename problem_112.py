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
#  1. ar is of type INTEGER ARRAY.
#  2. M is of type INTEGER.


def solve(arr,M):
    items_per_second = 0
    for fabric in arr:
        items_per_second +=  1 / fabric
        
    return int(math.ceil(M / items_per_second))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_count = int(input().strip())

    ar = []
    arItems = input().rstrip().split(" ")

    for i in range(ar_count):
        ar_item = int(arItems[i])
        ar.append(ar_item)

    M = int(input().strip())
    outcome = solve(ar, M)
    fptr.write(str(outcome)  + '\n')
    fptr.close()

