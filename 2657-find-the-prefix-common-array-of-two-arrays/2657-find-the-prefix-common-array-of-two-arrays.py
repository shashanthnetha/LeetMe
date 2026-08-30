class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        r=[]
        for i in range(len(A)):
            r.append(len(set(A[:i+1])&set(B[:i+1])))
        return r
        