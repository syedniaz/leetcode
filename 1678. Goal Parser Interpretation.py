class Solution:
    def interpret(self, command: str) -> str:
        str1 = ""
        for i, s in enumerate(command):
            if (s == "G"):
                str1 += "G"
            elif (s == "(" and command[i+1] == ')'):
                str1 += "o"
            elif (s == "(" and command[i+1] == 'a'):
                str1 += "al"
        return str1