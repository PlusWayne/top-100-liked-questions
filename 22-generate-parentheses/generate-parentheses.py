class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        left, right, string, res = n, n, '', []
        self.dfs(left, right, string, res)
        return res
    
    def dfs(self, left, right, string, res):
        if right < left:  # 去掉不可能的分支
            return  
        if not right and not left:
            res.append(string)
            return
        if left:  # 如果left用完就再也没有分支了
            self.dfs(left-1, right, string+'(', res)
        if right:
            self.dfs(left, right-1, string+')', res)
