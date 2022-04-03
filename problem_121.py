#!/bin/python3

import re
import sys
import math
import random
import os
from heapq import heappush, heappop


#
# implement method/function with name 'minStation' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. ar is of type INTEGER ARRAY.
#  2. de is of type INTEGER ARRAY.


class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.left < other.left
        

def minStation(ar,de):
    if len(ar) == 0:
        return 0
        
    intervals = []
    for idx in range(len(ar)):
        intervals.append(Interval(ar[idx], de[idx]))
        
    intervals.sort(key=lambda x: x.left)
    min_heap = []
    heappush(min_heap, intervals[0])
    result_count = 1
    for idx in range(1, len(intervals)):
        curr_size = len(min_heap)
        result_count = max(result_count, curr_size)
        while len(min_heap) and  min_heap[0].right < intervals[idx].left:
            heappop(min_heap)
        
        heappush(min_heap, intervals[idx])
        
    result_count = max(result_count, len(min_heap))
    return result_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    ar_count = int(input().strip())

    ar = []
    arItems = input().rstrip().split(" ")

    for i in range(ar_count):
        ar_item = int(arItems[i])
        ar.append(ar_item)

    de_count = int(input().strip())

    de = []
    deItems = input().rstrip().split(" ")

    for i in range(de_count):
        de_item = int(deItems[i])
        de.append(de_item)

    outcome = minStation(ar, de)

    fptr.write(str(outcome)  + '\n')

    fptr.close()

