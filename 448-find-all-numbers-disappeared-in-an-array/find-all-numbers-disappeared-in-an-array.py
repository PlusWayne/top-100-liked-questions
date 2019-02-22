class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        # return list(set(range(1,len(nums)+1)) - set(nums))
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1]) 
            #将数组中有的值的位置都标记为负号
            #那么没标记到的位置就是缺的值
        return [i+1 for i in range(len(nums)) if nums[i]>0]
