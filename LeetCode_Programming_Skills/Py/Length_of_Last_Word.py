class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        arr_filtered = [i for i in arr if i != ""]
        return len(arr_filtered[-1])
