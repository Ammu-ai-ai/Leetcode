class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        from collections import Counter
        
        count = Counter(s)
        length = 0
        odd_found = False
        
        for c in count.values():
            length += (c // 2) * 2
            if c % 2 == 1:
                odd_found = True
        
        if odd_found:
            length += 1
            
        return length