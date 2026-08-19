class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = set(map(tuple, reservedSeats))
        ans = 0

        rows = set(row for row, seat in reservedSeats)

        # Rows with no reserved seats
        ans += (n - len(rows)) * 2

        for row in rows:

            left = all((row, seat) not in reserved for seat in range(2, 6))
            right = all((row, seat) not in reserved for seat in range(6, 10))
            middle = all((row, seat) not in reserved for seat in range(4, 8))

            if left and right:
                ans += 2

            elif left or right or middle:
                ans += 1

        return ans