class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        r = []

        for i in range(len(grid)):
            if i % 2 == 0:
                r += grid[i]
            else:
                r += grid[i][::-1]

        return r[::2]

        