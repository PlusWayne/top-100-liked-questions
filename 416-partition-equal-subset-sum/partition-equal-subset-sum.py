class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = int(sum(nums)/2)
        dp = [0] * (target+1)
        dp[0] = 1
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j] = dp[j] or dp[j-num]
        return True if dp[-1]==1 else False
