class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Counts the number of prime numbers less than a non-negative int n
        Returns the count of primes
        '''
        primes = [True for i in range(n+1)] #Time Complexity O(n), Space Complexity O(n)
        p = 2
        count = 0
        while p * p < n: #Only need to check up to sqrt(n)
            if primes[p] == True:
                for i in range(p * p, n + 1, p): #Mark larger products of seen value
                    primes[i] = False
            p += 1
        for p in range(2, n): #Count remaining prime spaces
            if primes[p]:
                count += 1
        return count