class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        # r = set()

        # for i in range(len(nums) - 2):
        #     left = i + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]

        #         if total == 0:
        #             r.add((nums[i], nums[left], nums[right]))
        #             left += 1
        #             right -= 1

        #         elif total < 0:
        #             left += 1

        #         else:
        #             right -= 1

        # return [list(x) for x in r]
        nums.sort()
        r=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        r.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return [list(x) for x in r]

        