class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=[]
        coloum=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    coloum.append(j)
        for i in set(row):
            matrix[i]=[0]*len(matrix[0])
        for j in coloum:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        