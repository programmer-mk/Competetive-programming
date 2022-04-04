#!/bin/python3

import re
import sys
import math
import random
import os
from collections import deque


#
# implement method/function with name 'solve' below.
#
# The function is expected to return a value of type STRING.
# The function accepts following parameters:
#  1. S is of type STRING.


"""
    ABC
    
    
   1. ["A"]
   2. ["A B", "AB"]
   3. ["A B C", "A BC", "AB C", "ABC"]
"""


def format_output(list):
    result = [ '(' + elem + ')' for elem in list]
    return "".join(result)

def solve(word):
    queue = deque()
    queue.append(word[0])
    
    for idx in range(1, len(word)):
        curr_size = len(queue)
        for _ in range(curr_size):
            elem = queue.popleft()
            queue.append(elem+" "+word[idx])
            queue.append(elem+word[idx])
        
    return format_output(list(queue))    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    S = input()

    outcome = solve(S)

    fptr.write(str(outcome)  + '\n');

    fptr.close()

