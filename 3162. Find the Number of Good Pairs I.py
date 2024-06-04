class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=0
        n = len(nums1)
        m = len(nums2)
        for i in nums1:
            for j in nums2:
                div = j*k
                if (i % div == 0):
                    pairs = pairs+1
        return pairs
        