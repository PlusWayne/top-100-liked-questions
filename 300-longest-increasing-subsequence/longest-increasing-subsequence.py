class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1,len(dp)):
            maxval = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    maxval = max(maxval, dp[j])
            
            dp[i] = maxval + 1
        return max(dp)
