class Solution 
{
    /* First attempt*/
    /* Works, but is too slow*/
//     public int longestConsecutive(int[] nums) 
//     {
//         // Hash initial array for fast lookup
//         HashSet<Integer> check = new HashSet<Integer>();
//         for (int num : nums)
//             check.add(num);
        
//         // Find longest consecutive list of integers
//         int longest = 0;
//         for (int num : check)
//         {
//             int upper = nums[i]+1, lower = nums[i]-1;
//             while (check.contains(upper)) // Check above mid
//                 upper += 1;
//             while (check.contains(lower)) // Check below mid
//                 lower -= 1;
//             longest = Math.max((upper-lower)-1, longest);
//         }
        
//         return longest;
//     }
    
    public int longestConsecutive(int[] nums)
    {
        // Hash initial array for fast lookup
        HashSet<Integer> check = new HashSet<Integer>();
        for (int num : nums)
            check.add(num);
        
        // Find longest consecutive list of integers
        int longest = 0;
        for (int num : check)
        {
            // Begin search at bottom of consecutive streak
            if (!check.contains(num-1)) 
            {
                int curr = num;
                int streak = 1;
                
                // Search for upper limit
                while (check.contains(curr+1)) 
                {
                    curr += 1;
                    streak += 1;
                }
                
                longest = Math.max(longest, streak);
            }
        }
        
        return longest;
    }
}