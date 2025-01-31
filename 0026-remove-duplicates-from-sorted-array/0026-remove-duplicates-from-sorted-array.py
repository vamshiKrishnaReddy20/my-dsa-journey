class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indexc = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[indexc] = nums[i]
                indexc += 1
        return indexc