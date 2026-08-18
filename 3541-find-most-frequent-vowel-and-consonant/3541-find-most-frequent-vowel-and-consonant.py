class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel={'a','e','i','o','u'}
        v=0
        const=0
        freq=defaultdict(int)
        for i in s:
            freq[i]+=1
        for char,count in freq.items():
            if char in vowel:
                v=max(v,count)
            else:
                const=max(const,count)
        return v+const