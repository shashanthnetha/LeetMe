class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum=max(nums)
        sum=0
        for _ in range(k):
            sum+=maximum
            maximum+=1
        return sum
            
        