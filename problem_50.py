class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        current = 0
        
        while(current < len(intervals) and intervals[current][1] < newInterval[0]):
            result.append(intervals[current])
            current += 1
            
        while(current < len(intervals) and intervals[current][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[current][0])
            newInterval[1] = max(newInterval[1], intervals[current][1])
            current += 1
            
        result.append(newInterval)
            
        while(current < len(intervals)):
            result.append(intervals[current])
            current += 1
            
        return result
            
        
            
        
            
        