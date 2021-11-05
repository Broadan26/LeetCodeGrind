class Solution 
{
    public void rotate(int[] nums, int k) 
    {
        int length = nums.length;
        int[] nums_copy = nums.clone();
        for (int i = 0; i < length; i++)
        {
            int move = (i + k) % length;
            nums[move] = nums_copy[i];
        }
    }
}