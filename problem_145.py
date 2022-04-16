from collections import deque

class Solution:
    
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {i: 0 for i in range(num_courses)}
        graph = {i: [] for i in range(num_courses)}
        result = []
        
        queue = deque()
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1
            
        for course in in_degree:
            if in_degree[course] == 0:
                queue.append(course)
                
        while queue:
            course = queue.popleft()
            result.append(course)
            for dependant in graph[course]:
                in_degree[dependant] -= 1
                if in_degree[dependant] == 0:
                    queue.append(dependant)
                    
        if len(result) != num_courses:
            return False
        else:
            return True
        
        