class Solution 
{
    public List<List<Integer>> permute(int[] nums) 
    {
        List<List<Integer>> answer = new ArrayList<>();
        if (nums.length < 1)
            return answer;
        
        permuteRec(nums, answer, new ArrayList<>(), new boolean[nums.length]);
        return answer;
    }
    
    public void permuteRec(int[] nums, List<List<Integer>> answer, List<Integer> current, boolean[] used)
    {
        if (current.size() == nums.length) // Permutation complete
        {
            answer.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = 0; i < nums.length; i++)
        {
            if (used[i]) continue;
            
            current.add(nums[i]); // Create new permutation
            used[i] = true;
            
            permuteRec(nums, answer, current, used); // Recurse
            
            used[i] = false; // Undo
            current.remove(current.size()-1);
        }
    }
}