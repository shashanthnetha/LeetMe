class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a=list(map(str,s.split()))
        return " ".join(a[:k])

        