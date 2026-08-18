class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        return [key for key, value in a.items() if value == 2]
        