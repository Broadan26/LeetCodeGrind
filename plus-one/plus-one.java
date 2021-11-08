class Solution 
{
    public int[] plusOne(int[] digits) 
    {
        for(int i = digits.length-1; i > -1; i--) // Start from back
        {
            if (digits[i] + 1 != 10) // Check for rollover
            {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0; // Rollover occurs
        }
        
        // Need to create new array to hold rollover of entire former array
        int[] newDigits = new int[digits.length+1];
        newDigits[0] = 1;
        return newDigits;
    }
}