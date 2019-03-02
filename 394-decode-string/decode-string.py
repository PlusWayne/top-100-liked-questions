class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack.append(['', 1])
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['',int(num)])
                print(stack)
                num = ''
            elif ch == ']':
                st, k = stack.pop()
                print(st)
                stack[-1][0] += k*st
            else:
                stack[-1][0] += ch
        return stack[0][0]
