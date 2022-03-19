import math
from heapq import *

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def  __lt__(self, other):
        return math.sqrt(other.x**2 + other.y**2) < self.distance_from_origin()
    
    def compare(self, other):
        return math.sqrt(other.x**2 + other.y**2) > self.distance_from_origin()

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def transform_to_list(self):
        return [self.x, self.y]
    

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for idx, point in enumerate(points):
            if idx < k:
                heappush(max_heap, Point(point[0], point[1]))
            else:
                if not max_heap[0].compare(Point(point[0], point[1])):
                    heappop(max_heap)
                    heappush(max_heap, Point(point[0], point[1]))
                    
        max_heap = [point.transform_to_list() for point in max_heap]
        return max_heap