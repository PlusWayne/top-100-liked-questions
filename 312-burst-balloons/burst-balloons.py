class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
#    complexity too high!!
#         if len(nums)==0:
#             return 0
#         nums = [1] + nums + [1]
#         return self.helper(nums)
        
#     def helper(self, nums: List[int]):
#         if len(nums)==3:
#             return nums[1]
#         temp = []
#         for i in range(1,len(nums)-1):
#             temp.append(nums[i-1] * nums[i] * nums[i+1] + self.helper(nums[:i]+nums[i+1:]))
#         return max(temp)
        nums = [1] + [num for num in nums if num >0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for k in range(2,n):
            for left in range(0, n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[i]*nums[left]*nums[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]
