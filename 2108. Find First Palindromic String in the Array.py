class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def reverse(s):
                str = ""
                for i in s:
                    str = i + str
                return str

        for w in words:
            r = reverse(w)
            if (w == r):
                return w
        return ""