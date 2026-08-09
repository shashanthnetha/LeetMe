class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        odd = False

        for i in set(s):
            if s.count(i) % 2 == 0:
                count += s.count(i)
            else:
                count += s.count(i) - 1
                odd = True

        if odd:
            count += 1

        return count

        