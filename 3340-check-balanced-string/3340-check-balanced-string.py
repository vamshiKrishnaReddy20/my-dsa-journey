class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        for i,ch in enumerate(num):
            if (i+1) % 2 == 0:
                even += int(ch)
            else:
                odd += int(ch)
        return odd == even