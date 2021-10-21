import java.util.HashMap;

class Solution 
{
    public int romanToInt(String s) 
    {
        // Handle empty strings
        if (s == null || s.length() == 0)
            return -1;
        
        // Create a hashmap for Roman numerals to equivalent ints
        HashMap<Character, Integer> Romans = new HashMap<Character, Integer>();
        Romans.put('I', 1);
        Romans.put('V', 5);
        Romans.put('X', 10);
        Romans.put('L', 50);
        Romans.put('C', 100);
        Romans.put('D', 500);
        Romans.put('M', 1000);
        
        // Run through the string mapping chars to ints
        int result = Romans.get(s.charAt(s.length()-1));
        for (int i = s.length()-2; i >= 0; i--)
        {
            //Next char is at least as big as previous
            if (Romans.get(s.charAt(i)) >= Romans.get(s.charAt(i+1)))
                result += Romans.get(s.charAt(i));
            
            //Next char is smaller than previous
            else
                result -= Romans.get(s.charAt(i));
        }
        return result;
    }
}