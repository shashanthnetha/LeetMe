class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # nums.sort()

        # ans = nums[k - 1] - nums[0]

        # for i in range(1, len(nums) - k + 1):
        #     diff = nums[i + k - 1] - nums[i]

        #     if diff < ans:
        #         ans = diff

        # return ans
        return  nums.sort() or min(R-L for L, R in zip(nums, nums[k-1:]))
        