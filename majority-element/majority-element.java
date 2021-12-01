class Solution 
{
    public int majorityElement(int[] nums) 
    {
        HashMap<Integer, Integer> count = new HashMap<>();
        
        for (int num : nums)
        {
            if (!count.containsKey(num))
                count.put(num, 1);
            else
                count.replace(num, count.get(num)+1);
        }
        
        int answer = -1, max = 0;
        for (Map.Entry<Integer, Integer> entry : count.entrySet())
        {
            if (entry.getValue() > max)
            {
                answer = entry.getKey();
                max = entry.getValue();
            }
        }
        
        return answer;
    }
}