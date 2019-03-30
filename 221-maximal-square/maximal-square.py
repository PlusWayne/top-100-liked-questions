class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # brute force
        # res = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]=='1':
        #             t = 1
        #             flag = True
        #             while i + t < len(matrix) and j + t < len(matrix[0]) and flag:
        #                 for x in range(j,j+t+1):
        #                     if matrix[i+t][x] == '0':
        #                         flag = False
        #                         break
        #                 for y in range(i,i+t+1):
        #                     if matrix[y][j+t] == '0':
        #                         flag = False
        #                         break
        #                 if flag:
        #                     t += 1
        #             res = max(res, t*t)
        # return res
        
        # DP
        if len(matrix)==0:
            return 0
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        res = 0
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                
                res = max(res, dp[i][j])
        return res*res
