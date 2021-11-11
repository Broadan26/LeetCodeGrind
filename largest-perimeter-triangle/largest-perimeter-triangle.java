class Solution 
{
    public int largestPerimeter(int[] nums) 
    {
        Arrays.sort(nums);    
        for (int i = nums.length-3; i >= 0; i--)
            if (validTriangle(nums[i], nums[i+1], nums[i+2]))
                return nums[i] + nums[i+1] + nums[i+2];
        return 0;
    }
    
    public boolean validTriangle(int a, int b, int c)
    {
        if (a + b <= c || a + c <= b || b + c <= a)
            return false;
        else
            return true;
    }
}