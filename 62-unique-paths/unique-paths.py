class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    
        prev = [1] * n   # first row
        
        for i in range(1, m):
            curr = [1] * n
            for j in range(1, n):
                curr[j] = curr[j-1] + prev[j]
            prev = curr
        
        return prev[-1]