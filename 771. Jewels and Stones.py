class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            for s in stones:
                if (j == s):
                    couns += 1
        return couns