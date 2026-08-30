class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums)):
            r.append(nums[nums[i]])
        return r
        