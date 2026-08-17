class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        a=nums[::2]
        b=nums[1::2]
        return sum(nums[::2])-sum(nums[1::2])
        