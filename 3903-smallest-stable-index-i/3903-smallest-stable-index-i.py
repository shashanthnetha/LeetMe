class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            a=max(nums[:i+1])
            b=min(nums[i:])
            if a-b<=k:
                return i
        else:
            return -1
        