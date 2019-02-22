class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        res = 0
        for j in J:
            res += S.count(j)
        return res
        # return sum(map(S.count, J))
