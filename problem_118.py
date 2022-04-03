#!/bin/python3

import re
import sys
import math
import random
import os
from copy import deepcopy


#
# implement method/function with name 'maze' below.
#
# The function is expected to return a value of type STRING ARRAY.
# The function accepts following parameters:
#  1. ar is of type INTEGER 2D ARRAY.


def maze_recursive(arr, N, i, j, curr_state, direction, result, visited):
    if i < 0 or i > N - 1 or j < 0 or j > N-1 or arr[i][j] == 0 or visited[i][j]:
        return

    visited[i][j] = True
    if i == 0 and j == 0:
        # starting point of execution path
        pass
    else:
        curr_state.append(direction)

    if i == N-1 and j == N-1:
        result.append("".join(curr_state.copy()))
        
        
    maze_recursive(arr, N, i+1, j, curr_state.copy(), 'D', result, deepcopy(visited))
    maze_recursive(arr, N, i, j+1, curr_state.copy(), 'R', result, deepcopy(visited))
    maze_recursive(arr, N, i-1, j, curr_state.copy(), 'U', result, deepcopy(visited))
    maze_recursive(arr, N, i, j-1, curr_state.copy(), 'L', result, deepcopy(visited))
    

def maze(arr):
    N = len(arr)
    if N == 0:
        return ""
    result = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    maze_recursive(arr, N, 0, 0, [], '', result, visited)
    result.sort()
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_rows = int(input().strip())
    ar_columns = int(input().strip())

    ar = []

    for i in range(ar_rows):
        sublist = []
        sublistInputItems = input().rstrip().split(" ")
        for j in range(ar_columns):
            sublist.append(int(sublistInputItems[j]))
        ar.append(sublist)
    outcome = maze(ar)

    for i in range(len(outcome)):
        fptr.write(str(outcome[i]))
        if i < len(outcome)-1:
            fptr.write(" ")
    fptr.write("\n")

    fptr.close()

