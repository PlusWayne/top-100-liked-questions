class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            res.append(bin(i).count('1'))
        return res
        
        # dynamic programming , very intersting
        # if num == 0:
        #     return [0]
        # res = [0] * (num + 1)
        # for i in range(1, num + 1):
        #     if i%2:
        #         res[i] = res[i-1] + 1
        #     else:
        #         res[i] = res[i/2]
        # return res
