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
