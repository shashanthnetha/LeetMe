
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=[]
        for i in nums:
            if i!=0:
                a.append(i)
        n=len(nums)-len(a)
        nums[:]=a+[0]*n
        
