class Solution 
{
    public List<String> commonChars(String[] words) 
    {
        // Setup answer and char count
        List<String> answer = new ArrayList<String>();
        int[] charCount = new int[26];
        Arrays.fill(charCount, Integer.MAX_VALUE);
        
        // Count characters in each word, find minimum common amount
        for (String word : words)
        {
            int[] lCount = new int[26];
            for (char ch : word.toCharArray())
                lCount[ch - 'a']++;
            for (int i = 0; i < 26; i++)
                charCount[i] = Math.min(charCount[i], lCount[i]);
        }
        
        // Convert number of chars to their char & string equivalents
        for (int i = 0; i < 26; i++)
        {
            while (charCount[i] > 0)
            {
            char temp = (char) (i + 97);
            answer.add(String.valueOf(temp));
            charCount[i]--;
            }
        }
        
        return answer;
    }
}