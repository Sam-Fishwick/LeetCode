#Given an integer array nums, return an array answer such that answer[i] is 
#equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
#integer.

#You must write an algorithm that runs in O(n) time and without using the 
#division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers: List[int] = [1 for i in range(0, len(nums))]
        
        prev: int = 1
        for i in range(0, len(nums)):
            answers[i] *= prev
            prev *= nums[i]
        
        post: int = 1
        for i in range(len(nums)-1, -1, -1):
            answers[i] *= post
            post *= nums[i]
        
        return answers
