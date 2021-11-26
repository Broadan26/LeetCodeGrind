class Solution 
{
    public List<List<Integer>> combinationSum3(int k, int n) 
    {
        List<List<Integer>> answer = new ArrayList<>();
        if (n > 45 || n < 0) // No solutions possible
            return answer;
        if (k < 1 || k > 9) // No solutions possible
            return answer;
        
        return generate(answer, new ArrayList<Integer>(), 1, k, n);
    }
    
    private List<List<Integer>> generate(List<List<Integer>> answer, List<Integer> current, int start, int k, int n)
    {
        if (n == 0 && k == 0) // Found a working combination
        {
            answer.add(new ArrayList<Integer>(current));
            return answer;
        }
        else if (k < 1 || n < 1) // Exceeded k nums, exceeded target sum
            return answer;
        
        // Generate combinations
        for (int i = start; i < 10; i++)
        {
            current.add(i);
            generate(answer, current, i+1, k-1, n-i);
            current.remove(current.size()-1);
        }
        
        return answer;
    }
}