class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        // Setup hash table and unique numbers array
        HashSet<Integer> numsSet = new HashSet<Integer>();
        int[] uniqueNums = new int[nums.length];
        
        // Find unique numbers
        for (int i = 0; i < nums.length; i++)
        {
            if (!numsSet.contains(nums[i]))
            {
                numsSet.add(nums[i]);
                uniqueNums[numsSet.size()-1] = nums[i];
            }
        }
        
        //Alter the original array
        for (int i = 0; i < numsSet.size(); i++)
            nums[i] = uniqueNums[i];
        
        // Return the size of the hash set
        return numsSet.size();
    }
}