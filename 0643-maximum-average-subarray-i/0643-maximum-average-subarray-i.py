class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # a=sum(nums[:k])
        # max_sum=a
        # for i in range(k,len(nums)):
        #     a+=nums[i]
        #     a-=nums[i-k]
        #     max_sum = max(max_sum, a)
        # return max_sum / k
        

        current_sum = sum(nums[:k])
        max_sum = current_sum

        left = 0
        right = k

        while right < len(nums):
            current_sum -= nums[left]
            current_sum += nums[right]

            max_sum = max(max_sum, current_sum)

            left += 1
            right += 1

        return max_sum/k
