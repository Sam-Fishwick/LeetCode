#You are given a large integer represented as an integer array digits, where 
#each digits[i] is the ith digit of the integer. The digits are ordered from 
#most significant to least significant in left-to-right order. The large integer
#does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        while digits[n] == 9:
            digits[n] = 0
            n -= 1
        if n < 0:
            digits = [1] + digits
        else:
            digits[n] += 1
        
        return digits

        return digits
