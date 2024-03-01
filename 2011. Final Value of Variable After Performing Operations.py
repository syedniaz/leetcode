class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for o in operations:
            if (o[0] == '-' or o[2] == '-'):
                count -= 1
            elif (o[0] == '+' or o[2] == '+'):
                count += 1
        return count