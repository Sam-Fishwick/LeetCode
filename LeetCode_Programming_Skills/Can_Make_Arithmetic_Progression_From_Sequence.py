class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        a = [arr[0]]
        d = arr[1] - arr[0]

        for i in range(1,len(arr)):
            a.append(a[i-1]+d)

        return True if arr == a else False
