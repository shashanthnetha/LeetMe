class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []

        for i in range(left, right + 1):

            valid = True

            for j in str(i):

                digit = int(j)

                if digit == 0 or i % digit != 0:
                    valid = False
                    break

            if valid:
                arr.append(i)

        return arr
        return arr

        