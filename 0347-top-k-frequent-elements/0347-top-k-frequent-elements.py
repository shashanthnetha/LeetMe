class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=k
        a=[]
        for i in sorted(Counter(nums),key=Counter(nums).get, reverse=True):
            n-=1
            a.append(i)
            if n==0:
                break
        return a
            