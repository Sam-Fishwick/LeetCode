#You are given two strings word1 and word2. Merge the strings by adding letters 
#in alternating order, starting with word1. If a string is longer than the other,
#append the additional letters onto the end of the merged string.

#Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged = ""

        if(len(word1)>=len(word2)):
            biggest = len(word1)
        else:
            biggest = len(word2)

        for i in range(0,biggest):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]

        return merged
