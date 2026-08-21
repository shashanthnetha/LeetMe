class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        for i in range(n):
            sum+=mat[i][i]
            sum+=mat[i][n-1-i]
        if n%2==1:
            sum-=mat[n//2][n//2]
        return sum
        