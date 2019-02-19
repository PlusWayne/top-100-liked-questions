class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        res = sorted(res.items(), key = lambda item: -item[1])
        return [res[i][0] for i in range(k)]
                
