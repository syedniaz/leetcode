class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for dets in details:
            age = int(dets[11]) * 10 + int(dets[12])
            if age > 60:
                count += 1
        return count