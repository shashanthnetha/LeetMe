class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
        n=len(nums)-len(a)
        b=["_"]*n
        nums[:]=a

        

        