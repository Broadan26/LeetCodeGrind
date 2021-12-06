class Solution 
{
    public int[] relativeSortArray(int[] arr1, int[] arr2) 
    {
        // Create a hashmap to store count of items in arr1
        // Use linked hashmap to preserve order
        HashMap<Integer, Integer> count = new LinkedHashMap<>();
        
        // Sort the array1
        Arrays.sort(arr1);
        for (int num : arr1)
            count.put(num, count.getOrDefault(num, 0)+1);
        
        // Create an answer array of length arr1 to store the results
        int answer[] = new int[arr1.length];
        
        // Fill the answer array based on arr2
        int loc = 0;
        for (int num : arr2)
        {
            for (int i = 0; i < count.get(num); i++)
                answer[loc++] = num;
            count.remove(num);
        }
        
        // Fill the answer array with what is left of arr1
        for (int num : count.keySet())
            for (int i = 0; i < count.get(num); i++)
                answer[loc++] = num;
        
        return answer;
    }
}