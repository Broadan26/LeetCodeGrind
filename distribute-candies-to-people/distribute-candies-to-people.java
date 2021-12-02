class Solution 
{
    public int[] distributeCandies(int candies, int numPeople) 
    {
        // Setup the answer and a candy to give counter
        int[] answer = new int[numPeople];
        int counter = 0;
        
        // Hand out candy taking the minimum of what to give / counter
        // Run while candies are available
        while (candies > 0)
        {
            answer[counter % numPeople] += Math.min(candies, counter+1);
            counter += 1;
            candies -= counter;
        }
        
        return answer;
    }
}