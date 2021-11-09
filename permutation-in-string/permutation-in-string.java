class Solution 
{
    public boolean checkInclusion(String s1, String s2) 
    {
        if (s1.length() > s2.length()) // Impossible
            return false;
        
        // Create an array map for s1
        int[] s1map = new int[26];
        for (int i = 0; i < s1.length(); i++)
            s1map[s1.charAt(i) - 'a'] += 1;
        
        // Create multiple s2 maps to compare with s1
        for (int i = 0; i <= s2.length() - s1.length(); i++)
        {
            int[] s2map = new int[26];
            for (int j = 0; j < s1.length(); j++)
                s2map[s2.charAt(i+j) - 'a'] += 1;
            if (match(s1map, s2map))
                return true;
        }
        return false;
    }
    
    public boolean match(int[] s1map, int[] s2map)
    {
        for(int i = 0; i < s1map.length; i++)
        {
            if(s1map[i] != s2map[i])
                return false;
        }
        return true;
    }
}