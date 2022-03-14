class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        result = []
        i , j, N, M  = 0, 0, len(firstList), len(secondList)
        while(i < N and j < M):
            first_overlap_second = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            second_overlap_first = firstList[i][0] <= secondList[j][0] and firstList[i][1] >= secondList[j][0]
            
            if first_overlap_second or second_overlap_first:
                curr_min = max(firstList[i][0], secondList[j][0])
                curr_max = min(firstList[i][1], secondList[j][1])
                result.append([curr_min, curr_max])
                                
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return result