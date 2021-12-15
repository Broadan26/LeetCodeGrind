class Solution 
{
    public String removeDuplicates(String s) 
    {
        // Create string builder to quickly build string
        StringBuilder answer = new StringBuilder();
        
        // Iterate the string and append chars to stringbuilder
        // If there is a consecutive match, delete the last element of the builder
        for (char ch: s.toCharArray())
        {
            int length = answer.length();
            if (length > 0 && answer.charAt(length-1) == ch)
                answer.deleteCharAt(length - 1);
            else
                answer.append(ch);
        }
        
        return answer.toString();
    }
}