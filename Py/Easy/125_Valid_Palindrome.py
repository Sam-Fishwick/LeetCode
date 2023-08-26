#A phrase is a palindrome if, after converting all uppercase letters into 
#lowercase letters and removing all non-alphanumeric characters, it reads the 
#same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        
        #return s == s[::-1] # True if s equal to it's reverse
        i: int = 0
        j: int = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i +=1
            j -= 1
        return True

