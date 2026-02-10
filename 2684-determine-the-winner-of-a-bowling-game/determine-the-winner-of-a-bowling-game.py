class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
      
        
      
        
        def score(player):
            total = 0
            bonus = 0
            
            for pins in player:
                if bonus > 0:
                    total += 2 * pins
                    bonus -= 1
                else:
                    total += pins
                
                if pins == 10:
                    bonus = 2
            
            return total
        
        s1 = score(player1)
        s2 = score(player2)
        
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0

