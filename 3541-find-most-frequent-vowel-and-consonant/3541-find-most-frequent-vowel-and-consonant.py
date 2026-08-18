class Solution:
    def maxFreqSum(self, s: str) -> int:
        a = defaultdict(int)
        b = defaultdict(int)
        vowels="aeiou"
        for i in s:
            if i in vowels:
                a[i]+=1
            else:
                b[i]+=1
        return max(a.values(),default=0)+max(b.values(),default=0)