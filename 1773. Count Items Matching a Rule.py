class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rk = 0
        rv = 0
        cnt = 0
        if (ruleKey == 'type'):
            rk = 0
        elif (ruleKey == 'color'):
            rk = 1
        elif (ruleKey == 'name'):
            rk = 2
        for i in items:
            if (i[rk] == ruleValue):
                cnt += 1
        return cnt