class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            total = sum(i)
            ans = max(ans, total)
        return ans
            
                