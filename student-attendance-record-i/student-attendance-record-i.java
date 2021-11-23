class Solution 
{
    public boolean checkRecord(String s) 
    {
        int countA = 0, countL = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s.charAt(i) == 'A') // Handle A
            {
                countA += 1;
                countL = 0;
                if (countA == 2) return false;
            }
            else if (s.charAt(i) == 'L') // Handle L
            {
                countL += 1;
                if (countL == 3) return false;
            }
            else
                countL = 0;
        }
        return countL == 3 ? false : true;
    }
}