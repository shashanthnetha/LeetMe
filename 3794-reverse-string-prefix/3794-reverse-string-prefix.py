class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        a=s[:k][::-1]+s[k:]
        return a
        
        