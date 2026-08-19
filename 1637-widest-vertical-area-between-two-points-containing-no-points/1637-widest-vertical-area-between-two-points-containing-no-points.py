class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a=[i[0] for i in points]
        a.sort()
        max_num=0
        for i in range(1,len(a)):
            if a[i]-a[i-1]>=max_num:
                max_num=a[i]-a[i-1]
        return max_num