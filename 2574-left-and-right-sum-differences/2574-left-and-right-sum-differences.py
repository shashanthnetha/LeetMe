class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            arr.append(abs(left-right))
        return arr