class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
   
        n = len(grid)
        N = n * n
        
        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6
        
        actual_sum = 0
        actual_sq_sum = 0
        
        for row in grid:
            for num in row:
                actual_sum += num
                actual_sq_sum += num * num
        
        diff = actual_sum - expected_sum          # a - b
        sq_diff = actual_sq_sum - expected_sq_sum # a^2 - b^2
        
        sum_ab = sq_diff // diff                 # a + b
        
        a = (diff + sum_ab) // 2
        b = a - diff
        
        return [a, b]

