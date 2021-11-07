class Solution 
{
    public String reverseWords(String s) 
    {
        // Split the words
        String words[] = s.split(" "); 
        
        // Reverse each word and concatenate into string builder
        StringBuilder answer = new StringBuilder();
        for (String word : words)
            answer.append(new StringBuffer(word).reverse().toString() + " ");
        return answer.toString().trim(); // Return reformatted string
    }
}