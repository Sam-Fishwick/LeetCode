class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        eq = 0
        inc = 0
        dec = 0
        
        for i in range(0,n-1):
            if nums[i] == nums[i+1]:
                eq += 1
            elif nums[i] < nums[i+1]:
                inc += 1
            elif nums[i] > nums[i+1]:
                dec += 1
        
        return True if ((eq+inc) == n-1) | ((eq+dec) == n-1) else False
