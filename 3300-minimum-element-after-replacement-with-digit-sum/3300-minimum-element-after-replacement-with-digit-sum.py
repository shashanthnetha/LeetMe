class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            digit_sum=sum(int(j) for j in str(i))
            arr.append(digit_sum)
        return min(arr)
        