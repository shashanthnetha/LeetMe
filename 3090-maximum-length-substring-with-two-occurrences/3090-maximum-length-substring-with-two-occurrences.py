class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        a={}
        left=0
        max_len=0
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]]=1
            else:
                a[s[i]]+=1
            while (max(a.values())>2):
                    a[s[left]]-=1
                    left+=1
                    if a[s[left]]==0:
                        a.remove[s[left]]
            max_len=max(max_len,i-left+1)
        return max_len
        
        