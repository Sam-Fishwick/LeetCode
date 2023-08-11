#Given two non-negative integers low and high. Return the count of odd numbers 
#between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count_odd: int = 0
        if (low%2!=0 and high%2!=0):
            return int((((high-low)+1)/2)+1)
        if (low%2==0 and high%2==0):
            return int((((high-low)+1)/2))
        if (low%2!=0):
            return int(((((high-low)+1)-2)/2)+1)
        else:
            return int(((high-low)/2)+1)
