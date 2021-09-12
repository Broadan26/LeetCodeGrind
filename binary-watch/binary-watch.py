class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        '''
        Given an integer indicating the number of LEDs on in a stopwatch
        Determines the possible times that could be shown by the stopwatch
        Returns the times as a list of strings
        '''
        
        answer = []
        if turnedOn < 0 or turnedOn > 8: #Not possible
            return answer

        for hour in range(0,12,1): #Iterate possible hours
            for minute in range(0,60,1): #Iterate possible minutes
                if (bin(hour) + bin(minute)).count('1') == turnedOn: #Count number of 1's present
                    answer.append('%d:%02d' % (hour,minute))
        return answer