class Solution:
    def replaceDigits(self, st: str) -> str:
        def shift(c, n):
            newN = ord(c)+n
            newC = chr(newN)
            return newC

        newSt = ""
        for i,s in enumerate(st):
            if (s.isdigit()):
                a = shift(st[i-1], int(s))
                newSt = newSt+a
            else:
                newSt = newSt+s
        return newSt