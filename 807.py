class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        s = 0
        grid_r = list(zip(*grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s += min(max(grid[i]), max(grid_r[j])) - grid[i][j]
        return s
