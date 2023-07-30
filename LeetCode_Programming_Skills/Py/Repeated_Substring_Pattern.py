#Given a string s, check if it can be constructed by taking a substring of it 
#and appending multiple copies of the substring together.

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in s[1:] + s[:-1]
