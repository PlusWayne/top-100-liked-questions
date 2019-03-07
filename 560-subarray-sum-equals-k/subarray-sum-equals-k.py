class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        cur = 0
        count = 0
        for num in nums:
            cur += num
            count += dic.get(cur-k,0)
            dic[cur] = dic.get(cur,0) + 1
        return count
