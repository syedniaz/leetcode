class Solution:
    def numberOfSteps(self, n: int) -> int:
        c = 0
        while (n != 0):
            if (n%2 == 0):
                n = n/2
                c = c+1
            else:
                n = n-1
                c = c+1
        return c