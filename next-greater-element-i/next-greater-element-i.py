class Solution:   
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer = []
        for num1 in nums1:
            i = 0
            while nums2[i] != num1: 
                i += 1
            for num2 in range(i, len(nums2)):
                if nums2[num2] > num1:
                    answer.append(nums2[num2])
                    break
            else:
                answer.append(-1)
        return answer