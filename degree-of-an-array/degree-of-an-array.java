class Solution 
{
    public int findShortestSubArray(int[] nums) 
    {
        if (nums.length < 1) // Not worth doing
            return 0;
        
        // Count occurrences of each value in nums & collect range info
        int maxCount = 0;
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
        for (int i = 0; i < nums.length; i++)
        {
            if (map.containsKey(nums[i])) // Update entry
            {
                ArrayList<Integer> info = map.get(nums[i]); // value
                int count = info.get(0); // Update count
                info.set(0, count+1);
                info.set(2, i); // Update end of range
                maxCount = Math.max(maxCount, info.get(0)); // Check max
            }
            else // Create new entry
            {
                ArrayList<Integer> info = new ArrayList<Integer>();
                info.add(1); // Count
                info.add(i); // Start range
                info.add(i); // End range
                map.put(nums[i], info);
                maxCount = Math.max(maxCount, info.get(0));
            }
        }
        
        // Find the smallest possible subarray
        int maxRange = Integer.MAX_VALUE;
        for (ArrayList<Integer> value : map.values())
            if (maxCount == value.get(0) && value.get(2) - value.get(1) < maxRange-1)
                maxRange = 1 + value.get(2) - value.get(1);

        return maxRange;
    }
}