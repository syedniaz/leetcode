class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            x = n
            for j in range(i+1, len(nums)):
                if (nums[j]+n == target):
                    z = []
                    z.append(i)
                    z.append(j)
        return z