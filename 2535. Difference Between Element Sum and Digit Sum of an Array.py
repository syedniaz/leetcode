class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = 0
        ds = 0
        for n in nums:
            es = es + n
            p = n
            if (p >= 10):
                while (p != 0):
                    ds = ds + p%10
                    p = int(p/10)
            else:
                ds = ds + p
        return abs(ds-es)