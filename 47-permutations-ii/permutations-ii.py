class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(idx):
            if idx == len(nums):
                ans.append(nums[:])
                return
            
            used = set()
            
            for i in range(idx, len(nums)):
                
                if nums[i] in used:
                    continue
                    
                used.add(nums[i])
                
                nums[idx], nums[i] = nums[i], nums[idx]
                
                backtrack(idx + 1)
                
                nums[idx], nums[i] = nums[i], nums[idx]

        ans = []
        backtrack(0)
        return ans