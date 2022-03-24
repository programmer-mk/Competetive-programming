from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = [-1] * 26
        visited = [False] * 26
        for idx, char in enumerate(s):
            last_index[ord(char) - ord('a')] = idx
            
        elem_stack = deque()
        for idx, char in enumerate(s):
            if idx > 0:
                if ord(char) > ord(elem_stack[0]):
                    if not visited[ord(char) - ord('a')]:
                        elem_stack.appendleft(char)
                        visited[ord(char) - ord('a')] = True    
                else:
                    if not visited[ord(char) - ord('a')]:
                        while len(elem_stack) > 0 and ord(char) <= ord(elem_stack[0]) and last_index[ord(elem_stack[0]) - ord('a')] > idx:
                            visited[ord(elem_stack[0]) - ord('a')] = False
                            elem_stack.popleft()
                        elem_stack.appendleft(char)
                        visited[ord(char) - ord('a')] = True  
            else:
                elem_stack.appendleft(char)
                visited[ord(char) - ord('a')] = True

                
        elem_stack = list(elem_stack)
        elem_stack.reverse()
        return "".join(elem_stack)
            
        