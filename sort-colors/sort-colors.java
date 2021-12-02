class Solution 
{
    /* Two Pass Solution*/
    public void sortColors(int[] nums) 
    {
        // Count the number of 0's, 1's, 2's
        int countZero = 0, countOne = 0, countTwo = 0;
        for (int num : nums)
        {
            if (num == 0) countZero++;
            else if (num == 1) countOne++;
            else countTwo++;
        }
        
        // Refill the array in sorted order
        int index = 0;
        while (countZero > 0)
        {
            nums[index] = 0;
            index++;
            countZero--;
        }
        while (countOne > 0)
        {
            nums[index] = 1;
            index++;
            countOne--;
        }
        while (countTwo > 0)
        {
            nums[index] = 2;
            index++;
            countTwo--;
        }
    }
}