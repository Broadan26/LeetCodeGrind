class Solution 
{
    public List<Integer> partitionLabels(String s) 
    {
        // Create a 2D array that holds the start of a char and its end
        // 0 = a, 25 = z
        int[] range = new int[26];
        
        // Create an array list to hold the ranges
        List<Integer> answer = new ArrayList<>();
        
        // Parse the string s and determine ranges of characters
        for (int i = 0; i < s.length(); i++)
            range[s.charAt(i) - 97] = i;
        
        // Setup a start and end for the range using i to iterate
        // Once a range has been found, save the range
        // Then move the start to i+1 for next range
        int end = 0, start = 0;
        for (int i = 0; i < s.length(); i++)
        {
            end = Math.max(end, range[s.charAt(i)-97]);
            if (end == i)
            {
                answer.add(i - start + 1);
                start = i + 1;
            }
        }
        
        return answer;
    }
}