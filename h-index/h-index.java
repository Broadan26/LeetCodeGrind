class Solution 
{
    public int hIndex(int[] citations) 
    {
        // Sort the array
        Arrays.sort(citations);
        
        // Track the current h
        int length = citations.length;
        
        // Find the first working instance of h
        for (int citation : citations)
        {
            if (length <= citation) return length;
            length -= 1;
        }
        
        return length;
    }
}