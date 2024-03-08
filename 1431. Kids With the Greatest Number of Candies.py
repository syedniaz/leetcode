class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = candies[0]
        for c in candies:
            if (c > max):
                max = c
        
        arr = []
        for c in candies:
            if (c+extraCandies >= max):
                arr.append(True)
            else:
                arr.append(False)
        return arr