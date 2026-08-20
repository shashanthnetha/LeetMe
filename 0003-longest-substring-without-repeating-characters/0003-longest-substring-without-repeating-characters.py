class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        for i in range(len(s)):
            a={}
            for j in range(i,len(s)):
                if s[j] in a:
                    break
                a[s[j]]=1
                max_count = max(max_count, len(a))
            
        return max_count
        



        