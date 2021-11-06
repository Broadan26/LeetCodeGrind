class Solution 
{
    public int[] twoSum(int[] numbers, int target) 
    {
        int[] answer = {-1, -1};
        HashMap<Integer,Integer> ht=new HashMap<Integer,Integer>();
        for (int i = 0; i < numbers.length; i++)
        {
            if (ht.containsKey(numbers[i]))
            {
                answer[0] = ht.get(numbers[i])+1;
                answer[1] = i+1;
                return answer;
            }
            else
                ht.put(target-numbers[i], i);
        }
        return answer;
    }
}