class Solution 
{
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) 
    {
        // Hash vertices that have incoming edges
        HashSet<Integer> incoming = new HashSet<>();
        for (List<Integer> edge : edges)
            incoming.add(edge.get(1));
        
        // Create a list to store vertices that have no incoming edges
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (!incoming.contains(i))
                answer.add(i);
        
        // Return the vertices without incoming edges
        return answer;
    }
}