class Solution 
{
    public int findJudge(int n, int[][] trust) 
    {
        // Create a hashset to store people who trust
        int[] isTrusting = new int[n];
        int[] isTrusted = new int[n];
        
        // Hash the number of people who trust & number of people someone is trusted by
        for (int[] trustor : trust)
        {
            // Temporarily store relationship
            int trusts = trustor[0];
            int trusting = trustor[1];
            
            // Update the relationships
            isTrusting[trusts-1] += 1;
            isTrusted[trusting-1] += 1;
        }
        
        // Check to see which number is both untrusting and has complete trust
        for (int current = 0; current < n; current++)
        {
            if (isTrusting[current] == 0 && isTrusted[current] == n-1)
                return current+1;
        }
        
        return -1;
    }
}