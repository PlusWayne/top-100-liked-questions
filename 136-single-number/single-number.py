class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        # for num in set(nums):
        #     if nums.count(num)==1:
        #         return num
        # for i in range(1,len(nums)):
        #     nums[i] = nums[i] ^ nums[i-1]
        # return nums[-1]
        res = 0
        for num in nums:
            res = res ^ num
        return res
