class Solution 
{
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        // No strings to work with
        if (strs == null || strs.length == 0) return new ArrayList<>();
        
        // Hashmap allows for quick comparing if anagram has been seen
        HashMap<String, List<String>> compare = new HashMap<>();
        
        // Iterate each word in the strs array
        for (String word : strs)
        {
            // Extract every char from the given word
            char[] ch = new char[26];
            for (char c : word.toCharArray())
                ch[c - 'a'] += 1;
            
            // Hash based on those chars to create unique keys for comparing anagrams
            String key = String.valueOf(ch);
            if (!compare.containsKey(key))
                compare.put(key, new ArrayList<>());
            compare.get(key).add(word);
        }
        
        return new ArrayList<>(compare.values());
    }
}