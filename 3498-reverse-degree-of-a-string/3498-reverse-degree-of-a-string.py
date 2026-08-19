class Solution:
    def reverseDegree(self, s: str) -> int:
        x=0
        for i in range(len(s)):
            x+=(ord('z') - ord(s[i]) + 1)*(i+1)
        return x
        