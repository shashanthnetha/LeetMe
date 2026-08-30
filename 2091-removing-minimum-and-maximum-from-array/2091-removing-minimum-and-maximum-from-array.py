class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a=nums.index(max(nums))
        b=nums.index(min(nums))
        n=len(nums)

        left=min(a,b)
        right=max(a,b)
        case1=right+1
        case2=n-left
        case3=(left+1)+(n-right)
        return min(case1,case2,case3)
        

        