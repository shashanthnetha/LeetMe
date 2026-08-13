class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n=k
        # a=[]
        # for i in sorted(Counter(nums),key=Counter(nums).get, reverse=True):
        #     n-=1
        #     a.append(i)
        #     if n==0:
        #         break
        # return a
        a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        b = sorted(a, key=a.get, reverse=True)
        return b[:k]
            