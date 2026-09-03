class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_smallest=float('inf')        
        for i in nums1:
            if i%2==1:
                odd_smallest=min(odd_smallest,i)
        if odd_smallest==float('inf'):
            return True
        for i in nums1:
            if i%2==0 and i<=odd_smallest:
                return False
        return True