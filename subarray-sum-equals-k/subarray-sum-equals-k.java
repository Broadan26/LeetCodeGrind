class Solution 
{
    public int subarraySum(int[] nums, int k)
    {
        // Track the current sum and number of matching subarrays
        int answer = 0;
        int currSum = 0;
        
        // Hashmap the sums and count their occurrences
        HashMap<Integer, Integer> sumMap = new HashMap<>();
        sumMap.put(0, 1);
        
        // Run through each num in nums and determine if they are a subarray equaling k
        for (int num : nums)
        {
            currSum += num;
            if (sumMap.containsKey(currSum - k))
                answer += sumMap.get(currSum - k);
            sumMap.put(currSum, sumMap.getOrDefault(currSum, 0)+1);
        }
        
        return answer;
    }
    
    /*
    public int subarraySum(int[] nums, int k) 
    {
        // Check each subarray variation and compare with k
        // Increase count if there is a match
        int answer = 0;
        for (int left = 0; left < nums.length; left++)
        {
            int currSum = 0;
            for (int right = left; right < nums.length; right++)
            {
                currSum += nums[right];
                if (currSum == k) answer += 1;
            }
        }
        return answer;
    }
    */
}