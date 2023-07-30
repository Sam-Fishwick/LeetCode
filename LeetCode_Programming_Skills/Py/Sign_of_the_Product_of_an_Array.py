#There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.

#You are given an integer array nums. Let product be the product of all values
#in the array nums.

#Return signFunc(product).

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
