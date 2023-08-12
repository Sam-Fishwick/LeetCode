#Given a square matrix mat, return the sum of the matrix diagonals.

#Only include the sum of all the elements on the primary diagonal and all the 
#elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum: int = 0
        for i, row in enumerate(mat):
            n = len(row)
            total_sum += row[i]
            if i != n-i-1:
                total_sum += row[n-i-1]
        return total_sum
        
