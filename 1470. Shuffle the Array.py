class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = []
        for i, num in enumerate(nums):
            if (n == len(nums)):
                continue
            else:
                newNums.append(num)
                newNums.append(nums[n])
                n += 1
        return newNums