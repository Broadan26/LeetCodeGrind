class Solution 
{
    public int countCharacters(String[] words, String chars) 
    {
        // Hash map the string chars to compare with other words
        HashMap<Character, Integer> charsCount = new HashMap<>();
        for (int i = 0; i < chars.length(); i++)
        {
            if (!charsCount.containsKey(chars.charAt(i)))
                charsCount.put(chars.charAt(i), 1);
            else
                charsCount.replace(chars.charAt(i), charsCount.get(chars.charAt(i))+1);
        }
        
        // Check each word in words
        int answer = 0;
        HashMap<Character, Integer> compare;
        for (String word : words)
        {
            // Create a shallow copy of the hashmap to compare with the word
            compare = (HashMap<Character, Integer>) charsCount.clone();
            boolean flag = true;
            
            // Check each char in the word
            for (char ch : word.toCharArray())
            {
                // Char is not preesent in chars
                if (compare.get(ch) == null || compare.get(ch) < 1)
                {
                    flag = false;
                    break;
                }
                else
                    compare.replace(ch, compare.get(ch)-1);
            }
            if (flag)
                answer += word.length();
        }
        
        return answer;
    }
}