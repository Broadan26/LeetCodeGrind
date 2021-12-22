class Solution 
{
    public String mergeAlternately(String word1, String word2) 
    {
        // Use stringbuilder to quickly build the strings
        StringBuilder answer = new StringBuilder();
        
        // Merge the strings at the same time
        int w1 = 0, w2 = 0;
        while (w1 < word1.length() && w2 < word2.length())
        {
            answer.append(word1.charAt(w1));
            answer.append(word2.charAt(w2));
            w1 += 1;
            w2 += 1;
        }
        
        // Finish merging whatever is left
        while (w1 < word1.length())
        {
            answer.append(word1.charAt(w1));
            w1 += 1;
        }
        while (w2 < word2.length())
        {
            answer.append(word2.charAt(w2));
            w2 += 1;
        }
        
        return answer.toString();
    }
}