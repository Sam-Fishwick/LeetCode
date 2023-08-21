#Given an integer array nums and an integer k, return the k most frequent 
#elements. You may return the answer in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        hash_count: dict = {}
        list_count: List[List[int]] = [[] for i in range(len(nums)+1)]

        for i in nums:
            hash_count[i] = 1 + hash_count.get(i,0)

        for key, value in hash_count.items():
            list_count[value].append(key)

        top_k: List[int] = []
        for i in range(len(list_count)-1, 0, -1):
            for n in list_count[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
