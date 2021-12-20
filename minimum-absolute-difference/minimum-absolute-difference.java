class Solution 
{
    public List<List<Integer>> minimumAbsDifference(int[] arr) 
    {
        // Sort the array to get nums in ascending order
        Arrays.sort(arr);
        
        // Find the minimum difference
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length-1; i++)
            minDiff = Math.abs(arr[i] - arr[i+1]) < minDiff ? Math.abs(arr[i] - arr[i+1]) : minDiff;
        
        // Generate the list of min difference pairs
        List<List<Integer>> diffList = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        for (int i = 0; i < arr.length-1; i++)
            if (Math.abs(arr[i] - arr[i+1]) == minDiff)
            {
                current.add(arr[i]);
                current.add(arr[i+1]);
                diffList.add(new ArrayList<>(current));
                current = new ArrayList<>();
            }
        
        return diffList;
    }
}