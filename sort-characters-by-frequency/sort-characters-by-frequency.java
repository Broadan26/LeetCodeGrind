class Solution 
{
    public String frequencySort(String s) 
    {
        // Use a hash map to count the number of characters in the string s
        HashMap<Character, Integer> map = new HashMap<>();
        for (char ch : s.toCharArray())
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        
        // Create a max heap to hold the most occurrences of a char at the top
        PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());
        maxHeap.addAll(map.entrySet());
        
        // Keep polling the heap until all elements are removed in order
        StringBuilder answer = new StringBuilder();
        while (!maxHeap.isEmpty())
        {
            Map.Entry entry = maxHeap.poll();
            for (int i = 0; i < (int)entry.getValue(); i++)
                answer.append(entry.getKey());
        }
        
        return answer.toString();
    }
}