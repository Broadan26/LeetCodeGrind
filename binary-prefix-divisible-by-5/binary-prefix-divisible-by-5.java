class Solution 
{
    public List<Boolean> prefixesDivBy5(int[] nums) 
    {
        // Create a boolean list to hold the answer
        List<Boolean> answer = new ArrayList<>();
        
        // Iterate the array of numbers performing bitshifts to track the prefixes
        int current = 0;
        for (int num : nums)
        {
            // Perform mod 5 at the same time to prevent overflow
            current = ((current << 1) | num) % 5;
            
            // Add to list if divisible by 5 (101)
            answer.add(current == 0);
        }
        
        return answer;
    }
}