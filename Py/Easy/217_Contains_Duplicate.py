#Given an integer array nums, return true if any value appears at least twice in
#the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        num_set: set = set()
    	
        for i in nums:
            if i in num_set:
                return True
            elif i not in num_set:
                num_set.add(i)

        return False
