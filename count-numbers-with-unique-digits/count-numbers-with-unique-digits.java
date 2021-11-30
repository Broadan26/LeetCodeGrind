class Solution 
{
    public int countNumbersWithUniqueDigits(int n) 
    {
        // Edge case
        if (n == 0) return 1;
        
        int answer = 10; // For n = 1
        int uniqueDigits = 9, availableNumbers = 9; //Setup arithmetic
        while (n > 1 && availableNumbers > 0)
        {
            uniqueDigits *= availableNumbers;
            answer += uniqueDigits;
            availableNumbers--;
            n--;
        }
        return answer;
    }
}