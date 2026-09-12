class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxSize = 0
        currentSize = 0

        def dfs(grid, i ,j):
            nonlocal currentSize
            currentSize+=1
            grid[i][j] = -1

            if i>0 and grid[i-1][j] == 1:
                dfs(grid, i-1, j)
            if i<n-1 and grid[i+1][j] == 1:
                dfs(grid, i+1, j)
            if j>0 and grid[i][j-1] == 1:
                dfs(grid, i, j-1)
            if j<m-1 and grid[i][j+1] == 1:
                dfs(grid, i, j+1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    maxSize = max(maxSize, currentSize)
                    currentSize = 0
        return maxSize

        