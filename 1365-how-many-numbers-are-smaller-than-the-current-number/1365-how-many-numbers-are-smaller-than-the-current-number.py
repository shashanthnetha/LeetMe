class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # arr=[]
        # # nums=sorted(nums)[::-1]
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if i!=j and nums[i]>nums[j]:
        #             count+=1
        #     arr.append(count)
        # return arr
        return [sorted(nums).index(i) for i in nums]
                    

        