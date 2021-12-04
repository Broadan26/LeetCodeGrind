class Solution 
{
    public String[] findOcurrences(String text, String first, String second) 
    {
        // Split the original text based on spaces
        String[] textSplit = text.split(" ");
        
        // Create a mutable list to store answers
        List<String> wordList = new ArrayList<>();
        
        // Check first two words to determine if adding third
        for (int i = 0; i < textSplit.length-2; i++)
        {
            if (textSplit[i].equals(first) && textSplit[i+1].equals(second))
                wordList.add(textSplit[i+2]);
        }
        
        // Convert the arraylist object to a string array
        String[] answer = new String[wordList.size()];
        answer = wordList.toArray(answer);
        
        return answer;
    }
}