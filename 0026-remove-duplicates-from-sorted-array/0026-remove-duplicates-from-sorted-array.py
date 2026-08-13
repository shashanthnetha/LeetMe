class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        n = len(nums) - len(a)

        b = ['_'] * n

        nums[:] = a + b

        return len(a)
        