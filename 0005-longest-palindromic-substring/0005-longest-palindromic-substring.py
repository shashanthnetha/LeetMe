class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                x = s[i:j+1]

                if x == x[::-1]:
                    if len(x) > len(ans):
                        ans = x

        return ans