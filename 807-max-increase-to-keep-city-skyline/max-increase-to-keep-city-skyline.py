class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        top = []
        left = []
        for i in range(len(grid)):
            top.append(max([tt[i] for tt in grid]))
            left.append(max(grid[i]))
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(top[j],left[i]) - grid[i][j]
        return res
        
