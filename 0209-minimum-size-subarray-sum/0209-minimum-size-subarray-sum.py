class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        min_count = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_count = min(min_count, right - left + 1)
                sum -= nums[left]
                left += 1

        if min_count == float('inf'):
            return 0

        return min_count

        