class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # for i in range(len(nums)):
        #     left=i
        #     right=len(nums)-1
        #     while left <right:
        #         if nums[left]-nums[right]<=limit:
        #             nums[left],nums[right]=nums[right],nums[left]
        #         right-=1
        # return nums
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i], i))

        arr.sort()

        ans = nums[:]

        start = 0

        while start < len(arr):

            end = start

            while end + 1 < len(arr) and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = []

            for i in range(start, end + 1):
                indices.append(arr[i][1])

            indices.sort()

            for i in range(len(indices)):
                ans[indices[i]] = arr[start + i][0]

            start = end + 1

        return ans