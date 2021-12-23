class Solution 
{
    public int distanceBetweenBusStops(int[] distance, int start, int destination) 
    {
        // Calculate the sum of the array initially
        int length = distance.length;
        int total = 0;
        for (int stop : distance)
            total += stop;
        
        // Find the sum of the distance going clockwise
        int clockwise = 0;
        while (start != destination)
        {
            clockwise += distance[start];
            start = (start + 1) % length;
        }
        
        // Using total sum & clockwise, determine whether clockwise or counterclockwise is better
        return Math.min(total - clockwise, clockwise);
    }
}