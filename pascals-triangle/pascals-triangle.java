class Solution 
{
    public List<List<Integer>> generate(int numRows) 
    {
        // Setup initial data structures
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        ArrayList<Integer> row = new ArrayList<Integer>();
        
        for(int i = 0; i < numRows; i++)
        {
            row.add(0, 1); // Add initial 1
            
            for(int j = 1; j < row.size()-1; j++) // Perform triangle operations
                row.set(j, row.get(j) + row.get(j+1));
            
            answer.add(new ArrayList<Integer>(row)); // Add a copy of row
        }
        
        return answer;
    }
}