class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        for n in nums:
            if (n < k):
                c = c+1
        return c