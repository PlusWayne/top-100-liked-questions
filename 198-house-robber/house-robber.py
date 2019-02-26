class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        prev_1 = nums[0]
        prev_2 = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            prev_1, prev_2 = prev_2, max(prev_1 + nums[i], prev_2)
        return prev_2
