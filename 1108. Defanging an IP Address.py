class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAdd = address.replace(".", "[.]")
        return newAdd