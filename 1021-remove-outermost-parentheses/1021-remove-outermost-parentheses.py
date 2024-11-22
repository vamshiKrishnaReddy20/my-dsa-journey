class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ''
        for i in s:
            if i == '(':
                if stack:
                    res += i
                stack.append(i)
            elif i == ')':
                stack.pop()
                if stack:
                    res += i
                    
        return res