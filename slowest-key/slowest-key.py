class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        '''
        Given a list of key release times and a list of keys pressed
        Determines the longest amount of time between key presses
        Returns the longest time between presses as a char
        '''
        start = 0 #Keeps track of previous key press
        max = 0 #Track the current max
        the_char = 'a' #Track the largest char lexicographically
        for idx in range(len(releaseTimes)): #Get the longest times for each character
            if (x:= releaseTimes[idx] - start) > max:
                max = x
                the_char = keysPressed[idx]
            elif (x:= releaseTimes[idx] - start) >= max and ord(keysPressed[idx]) > ord(the_char): #Longest by tiebreak
                max = x
                the_char = keysPressed[idx]
            start = releaseTimes[idx]
        return the_char