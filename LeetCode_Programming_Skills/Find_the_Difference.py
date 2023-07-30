class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        return "".join(set([i for i in t if s.count(i) != t.count(i)]))
        
