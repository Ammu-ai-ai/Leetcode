class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1:
            return n

        prev2 = 0   # F(0)
        prev1 = 1   # F(1)

        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1
