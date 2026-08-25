class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum=0
        while k!=0:
            a=max(nums)
            sum+=a
            nums.pop(-1)
            nums.insert(-1,a+1)
            k-=1
        return sum
            
        