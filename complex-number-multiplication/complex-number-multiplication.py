class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        index1 = num1.find('+') #Find the plus
        index2 = num2.find('+')
        int1 = int(num1[0:index1]) #Collect the first half
        int2 = int(num2[0:index2])
        ith1 = int(num1[index1 + 1: len(num1) - 1]) #Collect 2nd half
        ith2 = int(num2[index2 + 1: len(num2) - 1])
        answer1 = int1 * int2 #Collect constants
        answer2 = answer1 - (ith1 * ith2) #See if constants cancel
        answer3 = int1 * ith2 + int2 * ith1 #Determine constant before i

        return str(answer2) + '+' + str(answer3) + 'i'