class Solution 
{
    public String mostCommonWord(String paragraph, String[] banned) 
    {
        // Store banned words in a hashset for fast lookup
        HashSet<String> bannedSet = new HashSet<>();
        for (String ban : banned)
            bannedSet.add(ban);
        
        // Create hashmap to track most common word
        HashMap<String, Integer> map = new HashMap<>();
        
        // Convert all alphanumeric characters to lowercase equivalent for word comparison
        // Remove puncuation and replace with spaces
        String lower = paragraph.replaceAll("[^a-zA-Z0-9]", " ").toLowerCase();
        
        // Split the string based off of 1 or more white space characters
        String[] words = lower.split("\\s+");
        
        // Map each word to its numerical count in the string
        for (String word : words)
            if (!bannedSet.contains(word))
                map.put(word, map.getOrDefault(word, 0) + 1);
        
        // Find the most common word and return it
        int max = Integer.MIN_VALUE;
        String modeWord = "";
        for (String key : map.keySet())
            if (map.get(key) > max)
            {
                max = map.get(key);
                modeWord = key;
            }
        
        return modeWord;
    }
}