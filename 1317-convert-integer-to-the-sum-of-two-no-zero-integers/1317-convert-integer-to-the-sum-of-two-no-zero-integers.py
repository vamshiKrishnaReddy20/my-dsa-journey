class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if '0' not in str(n-i) and '0' not in str(i):
                return [i,n-i]