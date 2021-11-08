class Solution 
{
    public int strStr(String haystack, String needle) 
    {
        if (needle.length() == 0) // Empty needle
            return 0;
        
        int loc = 0;
        while (haystack.length() - loc >= needle.length())
        {
            if (haystack.charAt(loc) == needle.charAt(0)) // Found start of substring
            {
                int needleIdx = 1, hayIdx = loc+1; // Compare substrings
                while (needleIdx < needle.length() && needle.charAt(needleIdx) == haystack.charAt(hayIdx))
                {
                    needleIdx++;
                    hayIdx++;
                }
                if (needleIdx == needle.length()) // Substring completed/found
                    return loc;
            }
            loc++;
        }
        
        return -1; // Substring doesn't exist
    }
}