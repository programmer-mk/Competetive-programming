class Solution:
    
    def dfs(self, i, j, grid, visited):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or visited[i][j] or grid[i][j] == '0':
            return
        
        visited[i][j] = True
        self.dfs(i-1,j, grid, visited)
        self.dfs(i+1,j, grid, visited)
        self.dfs(i,j-1, grid, visited)
        self.dfs(i,j+1, grid, visited)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0
        M = len(grid)
        N = len(grid[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands_count += 1
                    self.dfs(i,j, grid, visited)
                    
                        
        return islands_count