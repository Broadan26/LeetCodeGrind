class Solution 
{
    public List<List<Integer>> threeSum(int[] nums) 
    {
        // Sort to make avoiding duplicates easier
        Arrays.sort(nums);
        
        // Run through each entry in the array
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < nums.length-2; i++)
        {
            if (i != 0 && nums[i] == nums[i-1]) continue;
            
            // Lock the current entry as the target
            // Setup two pointers to work towards finding 0
            int low = i+1, high = nums.length-1;
            int target = 0 - nums[i];
            while (low < high)
            {
                if (nums[low] + nums[high] == target) // Found a solution for 0
                {
                    answer.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    
                    // Iterate past duplicate answers
                    while (low < high && nums[low] == nums[low+1]) low += 1;
                    while (low < high && nums[high] == nums[high-1]) high -= 1;
                    low += 1;
                    high -= 1;
                }
                else if (nums[low] + nums[high] < target) low += 1;
                else high -= 1;
            }
        }
        
        return answer;
    }
}