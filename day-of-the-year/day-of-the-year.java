class Solution 
{
    private int[] monthDays = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    public int dayOfYear(String date)
    {
        // Split the string based on its delimiter
        String[] dateSplit = date.split("-");
        
        // Attempt to convert split strings to relevant integers
        // Take the sum of those integers
        int answer = -1;
        try
        {
            // Handle years as normal
            answer = Integer.valueOf(dateSplit[2]);
            for (int i = 0; i < Integer.valueOf(dateSplit[1])-1; i++)
                answer += monthDays[i];
            
            // Account for a leap year
            if (Integer.valueOf(dateSplit[0]) % 4 == 0 && Integer.valueOf(dateSplit[1]) > 2)
                answer += 1;
        }
        catch (NumberFormatException ex)
        {
            ex.printStackTrace();
        }
        
        return answer;
    }
}