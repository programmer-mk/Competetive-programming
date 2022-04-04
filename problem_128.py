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
#  1. X is of type STRING.
#  2. Y is of type STRING.


def solve(X,Y):
    maximum = 0
    M = len(X)+1
    N = len(Y)+1
    dp = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(1, M):
        for j in range(1, N):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maximum = max(maximum, dp[i][j])
            else:
                 dp[i][j] = 0

    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    X = input()
    Y = input()
    outcome = solve(X, Y)
    fptr.write(str(outcome)  + '\n')
    fptr.close()

