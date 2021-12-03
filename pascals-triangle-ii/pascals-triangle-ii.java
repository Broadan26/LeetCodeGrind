class Solution 
{
    public List<Integer> getRow(int rowIndex) 
    {
        // Create row to store answer
        List<Integer> answer = new ArrayList<>();
        answer.add(1);
        
        // Perform combinations to generate each Pascal column in the given row
        for (int col = 1; col <= rowIndex; col++)
            answer.add((int)((long)answer.get(answer.size()-1) * (rowIndex-(col-1))/col));
        
        return answer;
    }
}