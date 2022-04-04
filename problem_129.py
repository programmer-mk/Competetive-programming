#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'triplet' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. ar is of type INTEGER ARRAY.


def triplet(array):
    maximum = -math.inf
    N = len(array)
    array.sort()
    if array[0] >= 0:
        return array[-1]*array[-2]*array[-3]
    else:
        return max(array[-1]*array[-2]*array[-3], array[0]*array[1]*array[-1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_count = int(input().strip())
    ar = []
    arItems = input().rstrip().split(" ")
    for i in range(ar_count):
        ar_item = int(arItems[i])
        ar.append(ar_item)

    outcome = triplet(ar)
    fptr.write(str(outcome)  + '\n')
    fptr.close()

