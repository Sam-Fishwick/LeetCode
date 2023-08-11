#Given an integer n, return the number of prime numbers that are strictly less 
#than n.

class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0
        
        primes: list[bool] = [True] * n

        primes[0] = primes[1] = False

        for i in range(2,int((n**0.5)+1)):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        
        return sum(primes)
