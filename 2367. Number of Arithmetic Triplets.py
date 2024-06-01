class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = 0
        l = len(nums)
        for i in range(l):
            x = nums[i]
            for j in range(i+1, l):
                if (nums[j]- nums[i] == diff):
                    for k in range(j+1, l):
                        if(nums[k]-nums[j] == diff):
                            n = n+1
        return n