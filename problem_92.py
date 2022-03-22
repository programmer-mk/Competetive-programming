from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurencies = {}
        for num in nums:
            if occurencies.get(num):
                occurencies[num] += 1
            else:
                occurencies[num] = 1
                
        min_heap = []
        step = 0
        for key in occurencies:
            if step < k:
                heappush(min_heap, (occurencies[key], key))
            else:
                print(f'peek: {min_heap[0]}')
                peek_val, peek_key = min_heap[0]
                if occurencies[key] > peek_val:
                    heappop(min_heap)
                    heappush(min_heap, (occurencies[key], key))
                    
            step += 1
                    
        return [tup[1] for tup in min_heap]