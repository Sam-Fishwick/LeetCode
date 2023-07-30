class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hlen = len(haystack)
        nlen = len(needle)

        for i in range(0, hlen - nlen +1):
            if haystack[i:i+nlen] == needle:
                return i
        
        return -1
