class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        a={}
        ans=0
        while left<=right and right<len(nums):
            if nums[right] not in a:
                a[nums[right]]=1
                
            else:
                a[nums[right]]+=1
            right+=1
            while a[nums[right - 1]] > k:
                a[nums[left]]-=1
                left+=1
            ans=max(ans,right-left)
        return ans
                
        