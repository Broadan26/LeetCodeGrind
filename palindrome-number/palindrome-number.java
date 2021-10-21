class Solution 
{
    public boolean isPalindrome(int x) 
    {
        //Negatives are not palindromes
        if (x < 0) return false;
        
        int check = x;
        int new_x = 0;
        while (check > 0)
        {
            new_x = (new_x * 10) + (check % 10);
            check = check / 10;
        }
        return (new_x == x);
    }
}