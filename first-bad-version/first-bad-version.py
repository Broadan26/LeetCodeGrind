# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        Utilizes isBadVersion API and Binary Search to find the first instance of a bad version
        Returns the first instance of a bad version as an int
        '''
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid): #Bad version is lower
                high = mid
            else: #Bad version is higher
                low = mid + 1
        return low