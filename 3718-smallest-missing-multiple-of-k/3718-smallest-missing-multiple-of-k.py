class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=1
        while n>0:
            if n*k not in nums:
                return n*k
            n+=1
        
        