class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr=[]
        for i,j in zip(nums,index):
            arr.insert(j,i)
        return arr