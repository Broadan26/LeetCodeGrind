class Solution 
{
    public int lengthOfLastWord(String s) 
    {
        int wordLength = 0;
        for (int i = s.length()-1; i > -1; i--)
        {
            if (wordLength == 0 && s.charAt(i) == ' ')
                continue;
            else if (s.charAt(i) != ' ')
                wordLength += 1;
            else
                break;
        }
        return wordLength;
    }
}