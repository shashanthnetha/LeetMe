class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        a=str(n)
        s=0
        for i in set(a):
            s+=int(i)*(a.count(i))
        return s
        