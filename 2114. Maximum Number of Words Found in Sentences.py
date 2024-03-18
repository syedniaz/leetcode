class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        nums = []
        for sen in sentences:
            num = 1
            for s in sen:
                if (s == ' '):
                    num += 1
            nums.append(num)
        nums.sort()
        return nums[len(nums)-1]