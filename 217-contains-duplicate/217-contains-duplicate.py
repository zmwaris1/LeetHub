class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for i in d:
            value = d[i]
            if value>1:
                return True
            else:
                False