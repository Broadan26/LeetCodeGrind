class Solution 
{
    public int[] intersect(int[] nums1, int[] nums2) 
    {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>(); // Map nums1 & counts
        ArrayList<Integer> answer = new ArrayList<Integer>(); // For final answer
        
        // Map nums1
        for (int i = 0; i < nums1.length; i++) 
        {
            hm.put(nums1[i], hm.getOrDefault(nums1[i], 0) + 1);
        }
        
        //Intersect nums1 with nums2
        for (int i = 0; i < nums2.length; i++)
        {
            if (hm.containsKey(nums2[i]) && hm.get(nums2[i]) > 0)
            {
                answer.add(nums2[i]);
                hm.put(nums2[i], hm.get(nums2[i])-1);
            }
        }
        
        // Convert arraylist to array to return
        int[] result = new int[answer.size()];
        for (int i = 0; i < result.length; i++)
            result[i] = answer.get(i);
        return result;
    }
}