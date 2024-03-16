class Solution:
    def minimumSum(self, n: int) -> int:
        nums = []
        while (n != 0):
            nums.append(n%10)
            n = int(n/10)
        nums.sort()
        num1 = nums[0]*10 + nums[2]
        num2 = nums[1]*10 + nums[3]
        return num1+num2