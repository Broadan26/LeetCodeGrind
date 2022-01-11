class Solution 
{
    public boolean canFinish(int numCourses, int[][] prerequisites) 
    {
        // Remember course connections and prerequisite counts
        int[][] matrix = new int[numCourses][numCourses];
        int[] inDegree = new int[numCourses];
        
        // Calculate prerequisite counts and memoize connections
        for (int i = 0; i < prerequisites.length; i++)
        {
            int preReq = prerequisites[i][0];
            int next = prerequisites[i][1];
            if (matrix[next][preReq] == 0)
                inDegree[preReq] += 1;
            matrix[next][preReq] = 1;
        }
        
        // Create a queue to hold all initial prerequisites
        int count = 0;
        Deque<Integer> queue = new LinkedList<>();
        for (int i = 0; i < inDegree.length; i++)
            if (inDegree[i] == 0)
                queue.addLast(i);
        
        // Run through the queue and count how number of in degrees that can be set to 0
        while (!queue.isEmpty())
        {
            int current = queue.removeFirst();
            count += 1; // Incremement courses taken
            for (int i = 0; i < numCourses; i++)
                if (matrix[current][i] != 0) // Remove prerequisite
                {
                    inDegree[i] -= 1;
                    if (inDegree[i] == 0) // If no more prereqs at all, add to queue
                        queue.addLast(i);
                }
        }
        
        return count == numCourses;
    }
}