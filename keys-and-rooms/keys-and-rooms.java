class Solution 
{
    public boolean canVisitAllRooms(List<List<Integer>> rooms) 
    {
        // Keep track of the rooms that have been visited
        HashSet<Integer> visited = new HashSet<>();
        visited.add(0);
        
        // Create a stack to hold the keys for rooms we can visit
        Deque<Integer> stack = new LinkedList<>();
        addToStack(stack, rooms.get(0), visited);
        
        // Visit the rooms using keys popped from the stack
        while (!stack.isEmpty())
        {
            int key = stack.removeLast();
            visited.add(key);
            addToStack(stack, rooms.get(key), visited);
        }
        
        // If any room was not visited, return false
        for (int i = 0 ; i < rooms.size(); i++)
            if (!visited.contains(i))
                return false;
        
        return true;
    }
    
    private void addToStack(Deque<Integer> stack, List<Integer> room, HashSet<Integer> visited)
    {
        for (int i = 0; i < room.size(); i++)
            if (!visited.contains(room.get(i)))
                stack.addLast(room.get(i));
    }
}