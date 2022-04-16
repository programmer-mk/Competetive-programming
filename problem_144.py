class Solution:
    
    def island_area_size(self, m, n, i, j, grid, visited):
        if i < 0 or i == n or j < 0 or j == m or visited[i][j] or not grid[i][j]:
            return 0
        
        visited[i][j] = True
        left = self.island_area_size(m, n, i, j-1, grid, visited)
        right = self.island_area_size(m, n, i, j+1, grid, visited)
        up = self.island_area_size(m, n, i-1, j, grid, visited)
        down = self.island_area_size(m, n, i+1, j, grid, visited)
        return 1 + left + right + up + down
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        max_area_size = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    current_area_size = self.island_area_size(m, n, i, j, grid, visited)
                    max_area_size = max(max_area_size, current_area_size)
        
        return max_area_size