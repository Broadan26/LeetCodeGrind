class Solution 
{
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) 
    {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        Set<Integer> set3 = new HashSet<>();
        
        // Hash nums1
        for (int num : nums1) 
            set1.add(num);
        
        // Hash nums2 and compare with nums1
        for (int num : nums2)
        {
            if (set1.contains(num) && !set2.contains(num))
            {
                answer.add(num);
                set2.add(num);
            }
            else set2.add(num);
        }
        
        // Compare nums1 and nums2 with nums3
        for (int num : nums3)
        {
            if (set1.contains(num) && set2.contains(num))
                continue;
            else if (set1.contains(num) && !set3.contains(num))
            {
                answer.add(num);
                set3.add(num);
            }
            else if (set2.contains(num) && !set3.contains(num))
            {
                answer.add(num);
                set3.add(num);
            }
        }
            
        return answer;
    }
}