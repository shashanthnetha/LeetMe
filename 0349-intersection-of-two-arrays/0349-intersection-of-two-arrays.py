class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        a=[]
        for i in nums1:
            if i not in a and i in nums2:
                a.append(i)
        return a