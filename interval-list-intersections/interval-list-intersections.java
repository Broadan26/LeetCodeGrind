class Solution 
{
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) 
    {
        List<int[]> answer = new ArrayList<>();
        int f = 0, s = 0;
        
        while (f < firstList.length && s < secondList.length)
        {
            // Find range of intersecting interval
            int min = Math.max(firstList[f][0], secondList[s][0]);
            int max = Math.min(firstList[f][1], secondList[s][1]);
            
            // If range is acceptable, append
            if (min <= max)
                answer.add(new int[]{min, max});
            
            // Move the iterators forward
            if (firstList[f][1] < secondList[s][1]) f += 1;
            else s += 1;
        }
        
        return answer.toArray(new int[answer.size()][]);
    }
}