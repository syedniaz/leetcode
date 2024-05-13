class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum = 0
        for i,s in enumerate(s):
            j = t.index(s)
            sum = sum + abs(i-j)
        return sum