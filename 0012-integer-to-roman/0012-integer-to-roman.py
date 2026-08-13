class Solution:
    def intToRoman(self, num: int) -> str:
        a = []

        while num >= 1000:
            num -= 1000
            a.append("M")

        while num >= 900:
            num -= 900
            a.append("CM")

        while num >= 500:
            num -= 500
            a.append("D")

        while num >= 400:
            num -= 400
            a.append("CD")

        while num >= 100:
            num -= 100
            a.append("C")

        while num >= 90:
            num -= 90
            a.append("XC")

        while num >= 50:
            num -= 50
            a.append("L")

        while num >= 40:
            num -= 40
            a.append("XL")

        while num >= 10:
            num -= 10
            a.append("X")

        while num >= 9:
            num -= 9
            a.append("IX")

        while num >= 5:
            num -= 5
            a.append("V")

        while num >= 4:
            num -= 4
            a.append("IV")

        while num >= 1:
            num -= 1
            a.append("I")

        return "".join(a)