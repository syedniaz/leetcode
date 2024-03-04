class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            j = i + 1
            if (j == len(nums)):
                break
            else:
                for j in range(j, len(nums)):
                    if (nums[i] == nums[j]):
                        count += 1
        return count