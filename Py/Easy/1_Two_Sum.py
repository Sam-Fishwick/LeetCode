#Given an array of integers nums and an integer target, return indices of the 
#two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not
#use the same element twice.

#You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums: dict = {}
        for i, val in enumerate(nums):
            complement: int = target - val
            if complement in hash_nums:
                return [i, hash_nums[complement]]
            hash_nums[val] = i
        return None
