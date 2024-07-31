class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        while len(nums) > 0:
            n = len(nums)
            averages.append(float((nums[0]+nums[n-1])/2))
            nums.pop(0)
            nums.pop()
        averages.sort()
        return averages[0]