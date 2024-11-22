class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stackLen = 0
        res = ''
        for i in s:
            if i == '(':
                if stackLen:
                    res += i
                stackLen += 1
            elif i == ')':
                stackLen -= 1
                if stackLen:
                    res += i

        return res