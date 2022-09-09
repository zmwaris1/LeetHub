class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxv = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i < j and nums[i] < nums[j]:
                    maxv = max(maxv, nums[j]-nums[i])
        return maxv if maxv > 0 else -1
        