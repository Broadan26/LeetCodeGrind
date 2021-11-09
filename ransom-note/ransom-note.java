class Solution 
{
    public boolean canConstruct(String ransomNote, String magazine) 
    {
        if (ransomNote.length() > magazine.length()) // Impossible
            return false;
        
        // Map the characters in the ransom note
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < magazine.length(); i++)
        {
            if (!map.containsKey(magazine.charAt(i)))
                map.put(magazine.charAt(i), 1);
            else
            {
                Integer count = map.get(magazine.charAt(i));
                map.replace(magazine.charAt(i), count+1);
            }
        }
        
        // Compare ransom note map to ransomNote
        for (int i = 0; i < ransomNote.length(); i++)
        {
            if (!map.containsKey(ransomNote.charAt(i))) // Char not in map
                return false;
            
            else if (map.get(ransomNote.charAt(i)) > 0) // Map has character
            {
                Integer count = map.get(ransomNote.charAt(i));
                map.replace(ransomNote.charAt(i), count-1);
            }
            
            else // Map val too low
                return false;
        }
        return true;
    }
}