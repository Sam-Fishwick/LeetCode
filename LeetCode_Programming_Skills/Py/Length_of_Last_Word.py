#Given a string s consisting of words and spaces, return the length of the last 
#word in the string.

#A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        arr_filtered = [i for i in arr if i != ""]
        return len(arr_filtered[-1])
