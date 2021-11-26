class Solution 
{
    public int countPrimes(int n) 
    {
        // Create array to hold list of primes
        boolean[] notPrime = new boolean[n];
        int count = 0;
        
        // Run through every number i -> n and check if seen as prime
        for (int i = 2; i < n; i++)
        {
            if (!notPrime[i]) // Found a prime, remove divisors of it
            {
                count += 1;
                for (int j = 2; i*j < n; j++)
                    notPrime[i*j] = true;
            }
        }
        return count;
    }
}