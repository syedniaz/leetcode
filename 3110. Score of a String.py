class Solution:
    def scoreOfString(self, st: str) -> int:
        p = 0
        for i, s in enumerate(st):
            if (i+1 != len(st)):
                p = p + abs(ord(s)-ord(st[i+1]))
        return p