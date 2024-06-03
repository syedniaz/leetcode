class Solution:
    def isValid(self, st: str) -> bool:
        stack = []
        for s in st:
            if s == '[' or s == '{' or s == '(':
                stack.append(s)
            else:
                if len(stack) == 0: 
                    return False
                if s == ']' and stack[-1] != '[':
                    return False
                if s == '}' and stack[-1] != '{':
                    return False
                if s == ')' and stack[-1] != '(':
                    return False
                stack.pop()
        return len(stack) == 0