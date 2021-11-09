class Solution 
{
    public int firstUniqChar(String s) 
    {
        // Map each character to an index, indicate repeats
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++)
        {
            if (!map.containsKey(s.charAt(i)))
                map.put(s.charAt(i), i);
            else
                map.replace(s.charAt(i), -1);
        }
        int min_value = Integer.MAX_VALUE;
        for (Object value: map.values())
        {
            if ((int)value < min_value && (int)value != -1)
                min_value = (int) value;
        }
        return min_value == Integer.MAX_VALUE ? -1 : min_value;
    }
}