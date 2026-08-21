class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        arr = [(value, index) for index, value in enumerate(nums)]
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            total = arr[left][0] + arr[right][0]

            if total == target:
                return [arr[left][1], arr[right][1]]
            elif total > target:
                right -= 1
            else:
                left += 1