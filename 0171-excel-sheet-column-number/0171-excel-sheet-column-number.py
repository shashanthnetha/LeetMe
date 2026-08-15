class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a=0
        for i in columnTitle:
            a = a * 26 + (ord(i) - 64)
        return a