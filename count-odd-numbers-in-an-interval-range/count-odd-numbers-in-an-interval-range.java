class Solution 
{
    public int countOdds(int low, int high) 
    {
        int answer = (high - low) / 2;
        if (low % 2 != 0 || high % 2 != 0) answer += 1;
        return answer;
    }
}