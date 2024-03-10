class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i,n in enumerate(nums):
            if (i == 0):
                continue
            else:
                nums[i] = nums[i-1] + nums[i]
        return nums