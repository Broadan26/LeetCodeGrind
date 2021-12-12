class Solution 
{
    public String multiply(String num1, String num2) 
    {
        // Multiplication by 0
        if (num1.equals("0") || num2.equals("0"))
            return "0";
        
        // Create an array to store products
        int[] answer = new int[num1.length() + num2.length() - 1];
        
        // Perform basic multiplication for every value
        for (int i = 0; i < num1.length(); i++)
            for (int j = 0; j < num2.length(); j++)
                answer[i+j] += (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
        
        // Shift the products up the array using basic addition
        for (int i = answer.length-1; i > 0; i--)
        {
            answer[i-1] += answer[i] / 10;
            answer[i] %= 10;
        }
        
        // Convert the int array into a string result
        StringBuilder build = new StringBuilder();
        for (int num : answer)
            build.append(num);
        
        return build.toString();
    }
}