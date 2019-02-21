class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = [[]]
        # for num in nums:
        #     temp = []
        #     for res in result:
        #         for i in range(len(res)+1):
        #             temp.append(res[:i] + [num] + res[i:])
        #     print(temp)
        #     result = temp
        # return result
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
