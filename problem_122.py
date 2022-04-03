#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'search' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. ar is of type INTEGER ARRAY.
#  2. K is of type INTEGER.


"""
    One Hiden test failing?? 
"""

def search(ar,K):
    if len(ar) == 0:
        return -1
    left = 0
    right = len(ar) - 1
    mid = 0
    founded = False
    while left <= right:
        mid = (left + right) // 2
        
        if mid > 0 and ar[mid] < ar[mid-1]:
            ar[mid], ar[mid-1] = ar[mid-1], ar[mid]
            
        if mid < len(ar)-1 and ar[mid] > ar[mid+1]:
            ar[mid], ar[mid+1] = ar[mid+1], ar[mid]
            
        if ar[mid] == K:
            founded = True
            break
        elif K < ar[mid]:
            right = mid-1
        else:
            left = mid + 1

    if founded:
        return mid
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_count = int(input().strip())

    ar = []
    arItems = input().rstrip().split(" ")

    for i in range(ar_count):
        ar_item = int(arItems[i])
        ar.append(ar_item)

    K = int(input().strip())
    outcome = search(ar, K)

    fptr.write(str(outcome)  + '\n')

    fptr.close()

