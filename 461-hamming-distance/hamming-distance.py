class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        diff = x ^ y
        return bin(diff).count('1')
        # ans = 0
        # while x or y:
        #     ans += (x % 2) ^ (y % 2)
        #     x //= 2
        #     y //= 2
        # return ans
