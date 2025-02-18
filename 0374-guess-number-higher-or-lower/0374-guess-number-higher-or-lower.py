# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while(True):
            mid = left + (right-left) // 2
            val = guess(mid)
            if not val:
                return mid
            elif val < 0:
                right = mid - 1
            else:
                left = mid + 1