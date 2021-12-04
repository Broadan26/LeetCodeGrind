class Solution 
{
    public int eraseOverlapIntervals(int[][] intervals) 
    {
        // No intervals to erase
        if (intervals.length < 1) return 0;
        
        // Sort the intervals with respect to their end values
        Arrays.sort(intervals, (a,b)->a[1]-b[1]);
        
        // Store the intervals start/end
        int prevStart = intervals[0][0], prevEnd = intervals[0][1];
        int answer = 0;
        
        // Compare new interval with previous interval
        // If overlap occurs, increment number to erase
        for (int i = 1; i < intervals.length; i++)
        {
            int currStart = intervals[i][0], currEnd = intervals[i][1];
            if (currStart <= prevStart || currStart < prevEnd)
                answer += 1;
            else
            {
                prevStart = currStart;
                prevEnd = currEnd;
            }
        }
        
        return answer;
    }
}