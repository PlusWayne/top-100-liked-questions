class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.dfs(sorted(nums), 0, [], res)
#         return res

        
        
    
#     def dfs(self, nums, index, path, res):
#         res.append(path)
#         for i in range(index,len(nums)):
#                self.dfs(nums, i+1, path+[nums[i]],res) 
    # def subsets(self, nums):
    #     res = []
    #     nums.sort()
    #     for i in range(1<<len(nums)):
    #         tmp = []
    #         for j in range(len(nums)):
    #             if i & 1 << j:  # if i >> j & 1:
    #                 tmp.append(nums[j])
    #         res.append(tmp)
    #     return res
       def subsets(self, nums: List[int]) -> List[List[int]]:
            res = [[]]
            for num in nums:
                res += [t+[num] for t in res]
            return res
