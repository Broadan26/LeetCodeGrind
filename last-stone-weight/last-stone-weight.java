class Solution 
{
    public int lastStoneWeight(int[] stones) 
    {
        if (stones.length < 2) // Array has only a single element
            return stones[0];
        
        int length = stones.length;
        Arrays.sort(stones);
        while(stones[length-2] != -1)
        {
            stones[length-1] = stones[length-1] - stones[length-2];
            stones[length-2] = -1;
            Arrays.sort(stones);
        }
        return stones[length-1];
    }
}