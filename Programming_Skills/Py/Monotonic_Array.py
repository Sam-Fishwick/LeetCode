#An array is monotonic if it is either monotone increasing or monotone decreasing.

#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
#An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

#Given an integer array nums, return true if the given array is monotonic, or 
#false otherwise.

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
