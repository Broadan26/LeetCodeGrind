class Solution 
{
    public int numSquares(int n) 
    {
        if (n < 0) return 0; // Not possible
        
        List<Integer> countPSquares = new ArrayList<Integer>();
        countPSquares.add(0);
        
        // Calculate all perfect squares including n
        while (countPSquares.size() <= n)
        {
            int m = countPSquares.size();
            int countSquares = Integer.MAX_VALUE;
            
            // Checks for nearest square roots based on previous results
            for (int i = 1; i * i <= m; i++) 
                countSquares = Math.min(countSquares, countPSquares.get(m - i*i)+1);
            countPSquares.add(countSquares);
        }
        
        return countPSquares.get(n);
    }
}