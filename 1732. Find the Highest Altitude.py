class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g = [0]
        for i, n in enumerate(gain):
            g.append(g[i]+n)
        return max(g)