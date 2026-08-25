class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        a,b,c=nums[-1],nums[-2],nums[0]
        return a+b-c
        