class Solution 
{
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) 
    {
        // Get each candy sum
        int aliceSum = 0, bobSum = 0;
        for (int candy : aliceSizes) aliceSum += candy;
        for (int candy : bobSizes) bobSum += candy;
        
        // Find difference between candy sums
        int diff = (aliceSum - bobSum) / 2;
        
        // Create a hash set of Alice's candies
        Set<Integer> aliceSet = new HashSet<Integer>();
        for (int candy : aliceSizes) aliceSet.add(candy);
        
        // Compare set of Alice with Bob's candies to find match
        for (int candy : bobSizes)
            if (aliceSet.contains(candy + diff))
                return new int[] {candy + diff, candy};
        
        return new int[] {-1, -1};
    }
}