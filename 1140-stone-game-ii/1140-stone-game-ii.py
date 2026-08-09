class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]
        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                if 2 * M >= n - i:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                for X in range(1, 2 * M + 1):
                    new_M = max(M, X)
                    current = suffix[i] - dp[i + X][new_M]

                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]
