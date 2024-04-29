class Solution:
    def finalString(self, st: str) -> str:
        st1 = ''
        for s in st:
            if (s == 'i'):
                st1 = st1[::-1]
            else:
                st1 = st1 + s
        return st1