class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = []
        for i, n in enumerate(nums):
            temp = 0
            for j in range (0, len(nums)):
                if (j != i):
                    if (n > nums[j]):
                        temp+=1
            num.append(temp)
        return num