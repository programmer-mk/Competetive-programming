#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'nQueen' below.
#
# The function is expected to return a value of type INTEGER ARRAY.
# The function accepts following parameters:
#  1. N is of type INTEGER.


def is_safe(N, board, i , j):
    for k in range(j):
        if board[i][k] == 1:
            return False
            
    for k in range(1, N):
        if i+k < N and j-k > -1 and board[i+k][j-k] == 1:
            return False
            
    for k in range(1, N):
        if i-k > -1 and j-k > -1 and board[i-k][j-k] == 1:
            return False
    
    return True

def n_queen_util(N, board, col, state, result):
    if col >= N:
        result.append(state)
        return True
        
    for i in range(N):
        if is_safe(N, board, i, col):
            board[i][col] = 1
            state.append(i+1)
            if n_queen_util(N, board, col+1, state.copy(), result):
                return True
            state.pop()
            board[i][col] = 0 
    
    return False
    
def n_queen(N):
    if N <= 0:
        return [-1]
    result = []
    board = [[0 for _ in range(N)] for _ in range(N)]
    if n_queen_util(N, board, 0, [], result):
        return result[0]
    else:
        return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    N = int(input().strip())
    outcome = n_queen(N)

    for i in range(len(outcome)):
        fptr.write(str(outcome[i]))
        if i < len(outcome)-1:
            fptr.write(" ")
    fptr.write("\n")

    fptr.close()

