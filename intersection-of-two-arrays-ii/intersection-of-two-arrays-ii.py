class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Given two lists of integers, generates a list of the intersecting values
        Returns the intersection as a list
        '''
        nums1Dict = {}
        nums2Dict = {}
        for num in nums1: #Hash the first list
            if num not in nums1Dict:
                nums1Dict[num] = 1
            else:
                nums1Dict[num] += 1
        for num in nums2: #Hash the second list
            if num not in nums2Dict:
                nums2Dict[num] = 1
            else:
                nums2Dict[num] += 1
        answer = []
        for key in nums1Dict: #Generate the intersection
            if key in nums2Dict:
                if nums1Dict[key] <= nums2Dict[key]:
                    answer.extend([key] * nums1Dict[key])
                else:
                    answer.extend([key] * nums2Dict[key])
        return answer