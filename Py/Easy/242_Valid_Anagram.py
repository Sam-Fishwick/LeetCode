#Given two strings s and t, return true if t is an anagram of s, and false 
#otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different
#word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        for i in s:
            if s.count(i) != t.count(i):
                return False
        
        return True
