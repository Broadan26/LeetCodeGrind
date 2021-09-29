class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pre = []
        post = [0] * len(nums)
        mult = 1

        # Product of numbers before the indice
        for i in range(0, len(nums)):
            if i == 0:
                pre.append(1)
            else:
                mult *= nums[i-1]
                pre.append(mult)

        # Product of numbers after the indice
        mult = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = 1
            else:
                mult *= nums[i+1]
                post[i] = mult
        
        # Product of both before and after indices
        for i in range(len(nums)):
            output.append(pre[i]*post[i])
        return output