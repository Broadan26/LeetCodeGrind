class Solution 
{
    public List<String> findRepeatedDnaSequences(String s) 
    {
        // String not long enough to have repeats
        if (s.length() < 10) return new ArrayList<>();
        
        // Create a hashset to store 10 letter variants
        HashSet<String> repeats = new HashSet<>();
        
        // Create a stringbuilder to quickly build 10 letter variants
        StringBuilder check = new StringBuilder();
        for(int i = 0; i < 9; i++)
            check.append(s.charAt(i));
        
        // Create list to store the repeated items
        HashSet<String> answer = new HashSet<>();
        
        // Iterate s starting from the first 10 letter variant
        // Check if it has been seen or not seen before
        int end = 9;
        while (end < s.length())
        {
            // String has not been seen before
            check.append(s.charAt(end));
            if (!repeats.contains(check.toString()))
                repeats.add(check.toString());
            
            // String has been seen before & is not already in the answer set
            else if (!answer.contains(check.toString()))
            {
                answer.add(check.toString());
                repeats.add(check.toString());
            }
            
            end += 1;
            check.deleteCharAt(0);
        }
        
        return new ArrayList(answer);
    }
}