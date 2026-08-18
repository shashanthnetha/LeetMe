class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a=list(map(int,date.split("-")))
        x=str(bin(a[0])[2:])+"-"+str(bin(a[1])[2:])+"-"+str(bin(a[2])[2:])
        return x