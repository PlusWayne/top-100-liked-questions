class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in set(nums):
        #     if nums.count(i) > n//2:
        #         return i
        
        # Moore voting algorithm
        res = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == res:
                count += 1
            elif count == 0:
                count += 1
                res = nums[i]
            else:
                count -= 1
        return res
                    
