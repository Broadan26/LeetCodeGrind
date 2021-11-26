class Solution 
{
    public int[] topKFrequent(int[] nums, int k) 
    {
        // Hash the count of the numbers in nums
        HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
        for (int num : nums)
        {
            if (!counts.containsKey(num))
                counts.put(num, 1);
            else
                counts.replace(num, counts.get(num)+1);
        }
        
        // Create a max heap based on the hashed counts
        Queue<Integer> maxHeap = new PriorityQueue<>(
            (n1, n2) -> counts.get(n1) - counts.get(n2));
        for (int num : counts.keySet())
        {
            maxHeap.add(num);
            if (maxHeap.size() > k) 
                maxHeap.poll();
        }
        
        // Poll the max heap for the k largest counts
        int[] answer = new int[k];
        for (int i = 0; i < k; i++)
            answer[i] = maxHeap.poll();
        
        return answer;
    }
}