#You are given an m x n integer grid accounts where accounts[i][j] is the amount
#of money the ith customer has in the jth bank. Return the wealth that the 
#richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totals: list[int] = []
        highest: int = 0
        big_i: int = 0
        
        for i, customer in enumerate(accounts):
            print(f"index {i}: {sum(customer)}")
            totals.append(sum(customer))
            if sum(customer) > highest:
                highest = sum(customer)
                big_i = i

        return totals[big_i]
