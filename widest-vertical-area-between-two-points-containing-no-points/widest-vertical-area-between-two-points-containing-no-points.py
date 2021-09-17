class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        '''
        Given a list of points, determine the max width between the vertical slices without a point between
        Returns the max width of the vertical slices
        '''
        points_set = set(x[0] for x in points) #Collect the x-values
        points_list = sorted(list(points_set)) #Make them accessible
        max_width = 0
        for num in range(len(points_list)-1): #Find max difference
            if (x := points_list[num+1] - points_list[num]) > max_width:
                max_width = x
        return max_width