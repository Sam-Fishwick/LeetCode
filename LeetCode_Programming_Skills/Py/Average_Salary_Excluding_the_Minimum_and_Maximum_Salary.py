#You are given an array of unique integers salary where salary[i] is the salary 
#of the ith employee.

#Return the average salary of employees excluding the minimum and maximum salary.
#Answers within 10**-5 of the actual answer will be accepted.

class Solution:
    def average(self, salary: List[int]) -> float:
        low: int = 0
        high: int = 0
        total: int = 0
        for employee in salary:
            total += employee
            if (low == 0) or (employee < low):
                low = employee
            if (employee > high):
                high = employee
        return (total-high-low)/(len(salary)-2)
