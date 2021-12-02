class Solution 
{
    public int[][] merge(int[][] intervals) 
    {
        // Sort the initial intervals so they can be merged cleanly
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));

        // Create an arraylist to hold the answer
        Deque<int[]> answer = new LinkedList<>();
        
        for (int[] interval : intervals)
        {
            // New interval does not overlap
            if (answer.size() < 1 || answer.getLast()[1] < interval[0])
                answer.add(interval);
            
            // New interval does overlap, find new top of range
            else
                answer.getLast()[1] = Math.max(answer.getLast()[1], interval[1]);
        }
        
        // Convert the linked list into an int[][] array
        return answer.toArray(new int[answer.size()][]);
    }
}