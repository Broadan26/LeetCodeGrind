class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
        int longest = 0;
        if (s.length() < 1) // No string exists
            return longest;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int hi = 0, lo = 0; hi < s.length(); hi++)
        {
            if (map.containsKey(s.charAt(hi))) // Update start of substring
                lo = Math.max(lo, map.get(s.charAt(hi))+1);
            map.put(s.charAt(hi), hi); 
            longest = Math.max(longest, hi-lo+1); // Update max
        }
        return longest;
    }
}