class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        mid = int(n/2)
        for index, character in enumerate(s[:mid]):
            temp = s[index]
            s[index] = s[n-index-1]
            s[n-index-1] = temp