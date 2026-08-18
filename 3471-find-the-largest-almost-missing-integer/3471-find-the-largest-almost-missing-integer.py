class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        a=nums[0]
        b=nums[-1]
        if k==len(nums):
            return max(nums)
        if k==1:
            arr= [i for i in nums if nums.count(i)==1]
        else:
            arr= [i for i in [a,b] if nums.count(i)==1]
        if arr:
            return max(arr)
        return -1
        

        