class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        l = len(nums)
        output = [0] * l
        temp = 1
        for i in range(l):
            output[i] = temp
            temp *= nums[i]
        temp = 1
        for i in reversed(range(l)):
            output[i] = temp * output[i]
            temp = temp * nums[i]
        return output
