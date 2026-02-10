class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
      
        
        def score(player):
            total = 0
            for i in range(len(player)):
                if (i - 1 >= 0 and player[i - 1] == 10) or (i - 2 >= 0 and player[i - 2] == 10):
                    total += 2 * player[i]
                else:
                    total += player[i]
            return total
        
        s1 = score(player1)
        s2 = score(player2)
        
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0
