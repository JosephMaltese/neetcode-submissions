class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        def explore(grid, i, j):
            grid[i][j] = 'X'
            if i>0 and grid[i-1][j] == '1':
                explore(grid, i-1, j)
            if i<len(grid)-1 and grid[i+1][j] == '1':
                explore(grid, i+1, j)
            if j>0 and grid[i][j-1] == '1':
                explore(grid, i, j-1)
            if j<len(grid[0])-1 and grid[i][j+1] == '1':
                explore(grid, i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandCount+=1
                    explore(grid, i, j)
        return islandCount