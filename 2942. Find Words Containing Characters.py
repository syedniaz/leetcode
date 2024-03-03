class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        i = 0
        arr = []
        for wo in words:
            cond = False
            for w in wo:
                if (w == x):
                    arr.append(i)
                    cond = True
                    break
            if cond:
                i += 1
                continue
            i += 1
        return arr