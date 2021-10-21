import java.util.HashMap;

class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        //Create hashmap for combinations
        HashMap<Integer, Integer> possible = new HashMap<Integer, Integer>();
        
        //Create array to store answer
        int[] answer = {-1, -1};
        
        for (int i = 0; i < nums.length; i++)
        {
            if (possible.containsKey(target - nums[i])) //Check if complement found
            {
                answer[0] = possible.get(target-nums[i]);
                answer[1] = i;
                break;
            }
            else // Add to hashmap for later
            {
                possible.put(nums[i], i);
            }
        }
        return answer;
    }
}