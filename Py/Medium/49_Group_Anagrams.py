#Given an array of strings strs, group the anagrams together. You can return the
#answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different
#word or phrase, typically using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs: dict = defaultdict(list)
        for s in strs:
            count: List[int] = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hash_strs[tuple(count)].append(s)
        return hash_strs.values()
