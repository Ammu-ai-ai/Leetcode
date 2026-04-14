class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        countA = 0
        consecutiveL = 0

        for ch in s:
            if ch == 'A':
                countA += 1
                if countA >= 2:
                    return False

            if ch == 'L':
                consecutiveL += 1
                if consecutiveL >= 3:
                    return False
            else:
                consecutiveL = 0  # reset if not 'L'

        return True