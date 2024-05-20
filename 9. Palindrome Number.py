class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        else:
            t = x
            rN = 0
            while (t != 0):
                d =  t % 10
                rN = rN * 10 + d
                t = int(t/10)
            if (x == rN):
                return True
            else:
                return False