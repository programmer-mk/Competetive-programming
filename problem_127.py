#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'swap' below.
#
# The function is expected to return a value of type STRING.
# The function accepts following parameters:
#  1. K is of type INTEGER.
#  2. S is of type STRING.


maximum = -1
    
def swap(K,S):

    def swap_recursive(K,S):
        global maximum
        if K == 0:
            return
            
        for i in range(len(S)-1):
            for j in range(i+1, len(S)):
                if S[i] < S[j]:
                    S[i], S[j] = S[j], S[i]
                    curr_num = int("".join(S))
                    if curr_num > maximum:
                        maximum = curr_num
                    swap_recursive(K-1,S)
                    S[i], S[j] = S[j], S[i]


    swap_recursive(K, list(S))
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    K = int(input().strip())
    S = input()

    outcome = swap(K, S)

    fptr.write(str(outcome)  + '\n');

    fptr.close()

