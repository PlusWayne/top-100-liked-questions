class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        add_zero = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.pop(i)
                add_zero += 1
        for i in range(add_zero):
            nums.append(0)
