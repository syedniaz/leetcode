class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ponts = []
        for p in points:
            ponts.append(p[0])
        ponts.sort()
        max = ponts[1] - ponts[0]
        for i,p in enumerate(ponts):
            if (i+1 == len(ponts)):
                continue
            else:
                if (ponts[i+1]-p > max):
                    max = ponts[i+1]-p
        return max