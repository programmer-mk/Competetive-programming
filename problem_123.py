#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'stairStep' below.
#
# The function is expected to return a value of type LONG INTEGER.
# The function accepts following parameters:
#  1. N is of type INTEGER.


def stairStep(N):
    dp = [1] * (N+1)
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[N] % (10**9 +7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    N = int(input().strip())
    outcome = stairStep(N)

    fptr.write(str(outcome)  + '\n')

    fptr.close()

