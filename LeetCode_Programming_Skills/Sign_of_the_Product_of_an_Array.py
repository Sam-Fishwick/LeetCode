class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        
        product = 1
        for i in nums:
            product *= i
        
        return 1 if product > 0 else -1 if product < 0 else 0
