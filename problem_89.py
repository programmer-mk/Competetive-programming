from collections import deque

class Solution:
    
    def generateParenthesis(self, n: int):
        solutions = set()
        solutions.add("()")
        if n == 1:
            return solutions
        
        queue = deque()
        queue.append("()")
        step = 2
        while step <= n:
            prev_level_size = len(queue)
            current_level_results = set()
            for i in range(prev_level_size):
                current = queue.popleft()
                
                for j in range(len(current)):
                    new_elem = current[:j]+"()"+ current[j:]
                    current_level_results.add(new_elem)
                    queue.append(new_elem)
                    
            solutions = current_level_results
            print(current_level_results)
            step += 1     
        return solutions