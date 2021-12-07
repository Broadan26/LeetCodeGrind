class Solution 
{
    public int nthSuperUglyNumber(int n, int[] primes) 
    {
        // Setup an array of ascending ugly numbers
        // Assign 1 to the first position
        int[] ugly = new int[n+1];
        ugly[0] = 1;
        
        // Setup an array to hold current prime products in primes
        int[] newPrimes = new int[primes.length];
        
        // Generate the next minimum product n times
        int index = 1;
        while (index < n)
        {
            // Generate next minimum product value based on prime products
            int min = Integer.MAX_VALUE;
            for (int i = 0; i < primes.length; i++)
                min = Math.min(min, ugly[newPrimes[i]] * primes[i]);
            ugly[index++] = min;
            
            // Skip past repeat products based on primes
            for (int i = 0; i < primes.length; i++)
                if (min == ugly[newPrimes[i]] * primes[i])
                    newPrimes[i]++;
        }
        
        return ugly[n-1];
    }
}