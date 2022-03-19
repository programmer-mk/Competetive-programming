from heapq import * 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for idx, num in enumerate(nums):
            if idx < k:
                heappush(min_heap, num)
            else:
                if (min_heap[0] < num):
                    heappop(min_heap)
                    heappush(min_heap, num)
                    
        return min_heap[0]