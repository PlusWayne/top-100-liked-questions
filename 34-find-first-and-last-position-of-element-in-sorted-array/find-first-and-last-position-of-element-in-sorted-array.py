class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findIndex(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, self.findIndex(nums, target, False)-1]

        
    
    def findIndex(self, nums, target, left):
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (left and nums[mid]==target):
                high = mid
            else:
                low = mid + 1
        return low
