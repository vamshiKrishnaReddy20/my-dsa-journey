class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        if (n == k):
            return -1
        total_a = 0
        total_b = 0
        total_c = 0
        for i in range(n):
            if s[i] == 'a':
                total_a += 1
            elif s[i] == 'b':
                total_b += 1
            else:
                total_c += 1
        if min(total_a ,total_b ,total_c) < k :
            return -1
            
        left = 0
        res = float("inf")

        for right in range(n):

            if s[right] == 'a':
                total_a -= 1
            elif s[right] == 'b':
                total_b -= 1
            else:
                total_c -= 1

            while min(total_a ,total_b ,total_c) < k:
                if s[left] == 'a':
                    total_a += 1
                elif s[left] == 'b':
                    total_b += 1
                else:
                    total_c += 1
                left += 1
            res = min(res,len(s) - (right - left + 1))
        return res

