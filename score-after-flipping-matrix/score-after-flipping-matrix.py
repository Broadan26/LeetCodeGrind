class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        '''
        Calculates the max possible binary sum of each row in a 2D list
        Returns the max sum as an integer
        '''
        if len(grid) == 0: #Grid is empty
            return 0

        #For rows, highest possible value is having a 1 in the first spot
        #If there isn't a 1, then flip the row
        for row in range(len(grid)):
            if grid[row][0] != 1: 
                for col in range(len(grid[0])):
                    grid[row][col] ^= 1

        #For columns, the highest possible value comes from having more 1's than 0's
        #So if there are not more 1's than 0's, flip the column
        for col in range(1, len(grid[0])):
            countOnes = 0
            for row in range(len(grid)): #Count the number of 1's
                if grid[row][col] == 1:
                    countOnes += 1

            if countOnes < (len(grid) / 2): #Flip 1's if less than half of total possible
                for row in range(len(grid)):
                    grid[row][col] ^= 1

        sum = 0
        for row in range(len(grid)): #Calculate the sum of each row
            value = 0
            for col in range(len(grid[0])):
                value = (value << 1) | grid[row][col]
            sum += value
        return sum