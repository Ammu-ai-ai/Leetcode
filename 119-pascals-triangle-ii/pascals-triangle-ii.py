class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        def fact(i):
            if i == 0 or i == 1:
                return 1
            return i * fact(i - 1)
        
        row = []
        for j in range(rowIndex + 1):
            res = fact(rowIndex) // (fact(j) * fact(rowIndex - j))
            row.append(res)
        
        return row

        