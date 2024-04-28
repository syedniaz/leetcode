class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        c = 0
        di = []
        while(n != 0):
            di.append(n%10)
            n = int(n/10)
        for d in di:
            if (num%d == 0):
                c = c+1
        return c