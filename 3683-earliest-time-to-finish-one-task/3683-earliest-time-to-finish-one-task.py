class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        arr=[]
        for i in tasks:
            arr.append(sum(i))
        return min(arr)
        