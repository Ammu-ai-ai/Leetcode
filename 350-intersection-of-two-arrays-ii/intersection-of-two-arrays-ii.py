class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
         
      
        seen = {}
        result = []

        # Count frequency in nums1
        for num in nums1:
            seen[num] = seen.get(num, 0) + 1

        # Check nums2 against the frequency map
        for num in nums2:
            if num in seen and seen[num] > 0:
                result.append(num)
                seen[num] -= 1

        return result
