class Solution 
{
    public List<List<Integer>> combine(int n, int k) 
    {
        List<List<Integer>> answer = new ArrayList<>();
        if (n < 1) // Nothing to do
            return answer;
        
        combinations(answer, new ArrayList<Integer>(), 1, n, k);
        return answer;
    }
    
    public void combinations(List<List<Integer>> answer, List<Integer> current, int start, int end, int k)
    {
        if (k == 0) // Combination complete
        {
            answer.add(new ArrayList<Integer>(current));
            return;
        }
        
        for (int i = start; i <= end; i++) // Generate combinations
        {
            current.add(i);
            combinations(answer, current, i+1, end, k-1);
            current.remove(current.size()-1);
        }
    }
}