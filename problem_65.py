class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)        
        start, end = 0, N-1
        while(start <= end):
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[start % N]
            