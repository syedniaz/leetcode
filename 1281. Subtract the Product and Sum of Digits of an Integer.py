class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while (n != 0):
            nums.append(n%10)
            n = int(n/10)
        s = 0
        p = 1
        for nn in nums:
            s += nn
            p *= nn
        return p-s