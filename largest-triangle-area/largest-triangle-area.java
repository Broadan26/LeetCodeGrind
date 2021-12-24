class Solution 
{
    public double largestTriangleArea(int[][] points) 
    {
        float max = 0;
        
        // Check all possible triangle areas
        // Use the formula for finding the area of a triangle given 3 points
        for (int A = 0; A < points.length-2; A++)
            for (int B = A+1; B < points.length-1; B++)
                for (int C = B+1; C < points.length; C++)
                {
                    float chunk1 = points[A][0] * (points[B][1] - points[C][1]);
                    float chunk2 = points[B][0] * (points[C][1] - points[A][1]);
                    float chunk3 = points[C][0] * (points[A][1] - points[B][1]);
                    
                    float current = Math.abs(.5f * (chunk1 + chunk2 + chunk3));
                    max = current > max ? current : max;
                }
        
        return max;
    }
}