class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum, temp = 0, 0
        for row in accounts:
            temp = 0
            for item in row:
                temp += item
            if (temp > sum):
                sum = temp
        return sum