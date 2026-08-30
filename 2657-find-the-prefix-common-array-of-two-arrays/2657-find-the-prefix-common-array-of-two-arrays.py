class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = [0] * len(A)
        prevs = set()
        prev = 0
        for i in range(len(A)):
            if A[i] in prevs:
                prev += 1
            else:
                prevs.add(A[i])
            if B[i] in prevs:
                prev += 1
            else:
                prevs.add(B[i])

            
            ans[i] = prev

        return ans