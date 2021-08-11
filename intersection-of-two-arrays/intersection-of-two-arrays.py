class Solution:
    def setIntersection(self, set1: set, set2: set) -> list[int]:
        return [x for x in set1 if x in set2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Given two arrays, finds the intersecting values of the arrays.
        Returns the intersection as an array of values.
        '''
        set1 = set(nums1) #Creates a set of the elements in the list
        set2 = set(nums2)
        if len(set1) < len(set2): #Compare the sets for commonalities
            return self.setIntersection(set1, set2)
        else:
            return self.setIntersection(set2, set1)