class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
   
        n, m = len(grid), len(grid[0])
        prev = [0] * m
        
        for i in range(n):
            curr = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                else:
                    up = grid[i][j] + (prev[j] if i > 0 else float('inf'))
                    left = grid[i][j] + (curr[j-1] if j > 0 else float('inf'))
                    curr[j] = min(up, left)
            prev = curr
        
        return prev[-1]