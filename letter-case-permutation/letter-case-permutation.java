class Solution 
{
    public List<String> letterCasePermutation(String s) 
    {
        List<String> answer = new ArrayList<>();
        if (s.length() < 1) // Nothing to do
            return answer;
        
        recurseString(s, answer, new StringBuilder());
        return answer;
    }
    
    public void recurseString(String s, List<String> answer, StringBuilder perm)
    {
        if (perm.length() == s.length()) // Permutation finished
        {
            answer.add(perm.toString());
            return;
        }
        
        if (Character.isLetter(s.charAt(perm.length()))) // Character is a letter
        {
            perm.append(Character.toLowerCase(s.charAt(perm.length()))); // Add lowercase letter
            recurseString(s, answer, perm);
            perm.deleteCharAt(perm.length()-1);
            
            perm.append(Character.toUpperCase(s.charAt(perm.length()))); // Add uppercase letter
            recurseString(s, answer, perm);
            perm.deleteCharAt(perm.length()-1);
        }
        else // Character is a number
        {
            perm.append(s.charAt(perm.length())); // Add digit
            recurseString(s, answer, perm);
            perm.deleteCharAt(perm.length()-1);
        }
    }
}