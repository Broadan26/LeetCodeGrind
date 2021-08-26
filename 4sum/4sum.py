class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Given a list of ints and a target, finds ways of 4 int sums to get the target
        Returns the possible solutions as a list of lists
        '''
        nums.sort() #Sort the list O(nlogn)
    
        def kSum(nums: list[int], target: int, k: int) -> list[list[int]]:
            answer = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return answer
            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        answer.append([nums[i]] + subset)
            return answer

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            new_list = []
            s = set()
            for i in range(len(nums)):
                if len(new_list) == 0 or new_list[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        new_list.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return new_list

        return kSum(nums, target, 4)