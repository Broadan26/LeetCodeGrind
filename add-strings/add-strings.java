class Solution 
{
    public String addStrings(String num1, String num2) 
    {
        // Create a carry and convert each string to char array for easy access
        int carry = 0;
        int n1Length = num1.length()-1, n2Length = num2.length()-1;
        char[] n1 = num1.toCharArray();
        char[] n2 = num2.toCharArray();
        
        // Create a string builder to save time concatenating
        StringBuilder build = new StringBuilder();
        
        while (n1Length >= 0 || n2Length >= 0 || carry == 1)
        {
            // Extract the individual character number
            int n1Temp = n1Length >= 0 ? (n1[n1Length] - '0') : 0;
            int n2Temp = n2Length >= 0 ? (n2[n2Length] - '0') : 0;
            
            // Perform integer addition and determine a carry
            int sum = n1Temp + n2Temp + carry;
            carry = sum / 10;
            
            // Add integer to string builder
            build.insert(0, sum % 10);
            n1Length -= 1;
            n2Length -= 1;
        }
        
        return build.toString();
    }
}