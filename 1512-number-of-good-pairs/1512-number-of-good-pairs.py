class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for val in count.values():
            result += val * (val-1)//2
        return result
        