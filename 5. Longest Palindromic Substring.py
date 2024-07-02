class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(st):
            return st == st[::-1]
        
        count = 1
        longest = s[0]
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if palindrome(s[i:j]):
                    if len(s[i:j]) > count:
                        count = len(s[i:j])
                        longest = s[i:j]
        
        return longest