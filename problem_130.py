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


def solve(ar):
    curr_sum = 0
    max_sum = -math.inf
    for end_window in range(len(ar)):
        curr_sum += ar[end_window]
        if curr_sum < 0:
            curr_sum = 0
        else:
            max_sum = max(max_sum, curr_sum)

    return max_sum

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

