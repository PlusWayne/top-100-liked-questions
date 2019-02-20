class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # res = 0
        # l = len(s)
        # for i in range(l):
        #     for j in range(i,l):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             res += 1
        # return res
        
        res = 0
        l = len(s)
        for center in range(2*l-1):
            left = center / 2
            right = left + center % 2
            while left>=0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
