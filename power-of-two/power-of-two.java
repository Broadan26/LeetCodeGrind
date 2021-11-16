class Solution 
{
    public boolean isPowerOfTwo(int n) 
    {
        if (n <= 0) return false; // Not power of 2
        return (n & (n-1)) == 0 ? true : false; // If 0, is power of 2
    }
}