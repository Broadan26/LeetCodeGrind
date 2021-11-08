class Solution 
{
    public String longestCommonPrefix(String[] strs) 
    {
        StringBuilder longest = new StringBuilder(); // Create a builder
        for(int i = 0; i < strs[0].length(); i++)
        {
            char current = strs[0].charAt(i);
            for (int j = 0; j < strs.length; j++)
            {
                if (strs[j].length() <= i || current != strs[j].charAt(i))
                    return longest.toString();
            }
            longest.append(current);
        }
        return longest.toString();
    }
}