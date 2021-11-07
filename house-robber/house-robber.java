class Solution 
{
    public int rob(int[] nums) 
    {
        int prevNo = 0;
        int prevYes = 0;
        for (int loot : nums)
        {
            int temp = prevNo;
            prevNo = Math.max(prevNo, prevYes);
            prevYes = loot + temp;
        }
        return Math.max(prevNo, prevYes);
    }
}