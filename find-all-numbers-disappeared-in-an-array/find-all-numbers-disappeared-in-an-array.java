class Solution 
{
    public List<Integer> findDisappearedNumbers(int[] nums) 
    {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++)
            if (!set.contains(nums[i]))
                set.add(nums[i]);
        
        List<Integer> answer = new ArrayList<Integer>();
        for (int i = 1; i <= nums.length; i++)
            if (!set.contains(i))
                answer.add(i);
        return answer;
    }
}