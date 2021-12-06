class Solution 
{
    public int longestPalindrome(String s) 
    {
        // Hash the provided string and count its characters
        HashMap<Character, Integer> sMap = new HashMap<>();
        for (char ch : s.toCharArray())
        {
            if (!sMap.containsKey(ch))
                sMap.put(ch, 1);
            else
                sMap.put(ch, sMap.get(ch)+1);
        }
        
        int length = 0;
        for (int value : sMap.values())
        {
            // Number of letters is even, just add to length
            if (value % 2 == 0)
                length += value;
            
            // Number of letters is odd & length is odd, add even number
            else if (length % 2 != 0)
                length += (value - 1);
            
            // Number of letters is odd & length is even, just add to length
            else
                length += value;
        }
        
        return length;
    }
}