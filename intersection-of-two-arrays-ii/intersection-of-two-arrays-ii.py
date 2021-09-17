class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Given two lists of integers, generates a list of the intersecting values
        Returns the intersection as a list
        '''
        from collections import Counter
        dict_nums1 = Counter(nums1)
        dict_nums2 = Counter(nums2)
        answer = []
        for i in dict_nums1:
            if i in dict_nums2:
                count_min = min(dict_nums1[i], dict_nums2[i])
                for _ in range(count_min):
                    answer.append(i)
        return answer
