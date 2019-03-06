class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for _ in range(len(nums)):
            if nums[index] == 2:
                nums.append(nums.pop(index))
            elif nums[index] == 0:
                nums.insert(0,nums.pop(index))
                index += 1
            else:
                index += 1
