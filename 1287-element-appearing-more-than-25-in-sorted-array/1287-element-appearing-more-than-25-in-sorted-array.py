class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        frequnecy = len(arr) // 4
        for i in range(len(arr)-frequnecy):
            if arr[i] == arr[i+frequnecy]:
                return arr[i]
        return -1
            