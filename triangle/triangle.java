class Solution 
{
    public int minimumTotal(List<List<Integer>> triangle) 
    {
        // Setup a list to store minimum paths taken
        List<Integer> minPaths = triangle.get(triangle.size()-1);
        
        // Starting from the bottom of triangle, work up finding the minimum path
        for (int level = triangle.size()-2; level > -1; level--)
            for (int i = 0; i <= level; i++)
                minPaths.set(i, Math.min(minPaths.get(i), minPaths.get(i+1)) + triangle.get(level).get(i));

        return minPaths.get(0);
    }
}