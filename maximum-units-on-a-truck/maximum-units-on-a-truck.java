class Solution 
{
    public int maximumUnits(int[][] boxTypes, int truckSize) 
    {
        // Sort the array by the number of units in each box
        Arrays.sort(boxTypes, (a,b) -> b[1] - a[1]);
        
        // Iterate through each box type and calculate the units to put on the truck
        // Take the min count of room on the truck or boxes available
        // Break early if truck out of room
        int answer = 0;
        for (int[] type : boxTypes)
        {
            int count = Math.min(truckSize, type[0]);
            answer += (count * type[1]);
            truckSize -= count;
            if (truckSize == 0) break;
        }
        
        return answer;
    }
}