class Solution 
{
    public int[][] kClosest(int[][] points, int k) 
    {
        // Create an array to hold the answer
        int[][] answer = new int[k][2];
        
        // Use euclidean distance to calculate the distance from the origin
        // Adjust the max heap based on the calculated distance
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> b[0] - a[0]);
        for (int i = 0; i < points.length; i++)
        {
            int[] entry = {findDistance(points[i]), i};
            if (maxHeap.size() < k)
                maxHeap.add(entry);
            else if (entry[0] < maxHeap.peek()[0])
            {
                maxHeap.poll();
                maxHeap.add(entry);
            }
        }
        
        // Fill up the answer array by polling the max heap
        for (int i = 0; i < k; i++)
            answer[i] = points[maxHeap.poll()[1]];
        
        return answer;
    }
    
    /* Calculates the euclidean distance of a point from the origin */
    private int findDistance(int[] point)
    {
        return (point[0] * point[0]) + (point[1] * point[1]);
    }
}