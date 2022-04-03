#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'distinctDigits' below.
#
# The function is expected to return a value of type INTEGER ARRAY.
# The function accepts following parameters:
#  1. ar is of type INTEGER ARRAY.


def distinct_digits(array):
    digits = {}
    for num in array:
        while num > 0:
            digit = num % 10
            if not digits.get(digit):
                digits[digit] = 1
            num = num // 10
            
    digits = list(digits)
    digits.sort()
    return digits
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_count = int(input().strip())

    ar = []
    arItems = input().rstrip().split(" ")

    for i in range(ar_count):
        ar_item = int(arItems[i])
        ar.append(ar_item)

    outcome = distinct_digits(ar)

    for i in range(len(outcome)):
        fptr.write(str(outcome[i]))
        if i < len(outcome)-1:
            fptr.write(" ")
    fptr.write("\n")

    fptr.close()

