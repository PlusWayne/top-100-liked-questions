class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            t = sorted(s)
            if tuple(t) not in res.keys():
                res[tuple(t)] = [s]
            else:
                res[tuple(t)].append(s)
        return list(res.values())
