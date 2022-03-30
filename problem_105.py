from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        N = len(arr)
        for idx, num in enumerate(arr):
            if idx < k:
                heappush(max_heap, (-abs(num - x), num))
            else:
                diff, val = max_heap[0]
                if -abs(num - x) > diff:
                    heappop(max_heap)
                    heappush(max_heap, (-abs(num - x), num))
                    
        result = [tup[1] for tup in max_heap]
        result.sort()
        return result
                    
        