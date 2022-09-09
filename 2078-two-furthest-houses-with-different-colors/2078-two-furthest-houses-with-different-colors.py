class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist_max = 0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] == colors[j]:
                    continue
                else:
                    dist_max = max(dist_max, abs(i-j))
        return dist_max
        