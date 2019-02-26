class Solution:
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[n-j-1][i], A[n-i-1][n-j-1], A[j][n-i-1] = \
                         A[n-j-1][i], A[n-i-1][n-j-1], A[j][n-i-1], A[i][j]
