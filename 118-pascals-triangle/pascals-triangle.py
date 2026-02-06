class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
    
        def fact(i):
            if i == 0 or i == 1:
                return 1
            return i * fact(i - 1)
        
        triangle = []
        
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                res = fact(i) // (fact(j) * fact(i - j))
                row.append(res)
            triangle.append(row)
        
        return triangle
   