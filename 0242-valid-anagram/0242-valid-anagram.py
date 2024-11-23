class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charCount = [0]*26

        for ch in s:
            charCount[ord(ch) - ord('a')] += 1
        for ch in t:
            charCount[ord(ch) - ord('a')] -= 1
        
        if any(charCount[val] != 0 for val in range(26)):
            return False
        return True