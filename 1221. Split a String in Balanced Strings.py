class Solution:
    def balancedStringSplit(self, ss: str) -> int:
        c = 0
        b = 0
        for s in ss:
            if s == 'R':
                b = b+1
            if s == 'L':
                b = b-1
            if b == 0:
                c +=1
        return c