class Solution:
    def convertDateToBinary(self, date: str) -> str:
        parts=date.split("-")
        year=bin(int(parts[0]))[2:]
        month=bin(int(parts[1]))[2:]
        day=bin(int(parts[2]))[2:]
        return year+"-"+month+"-"+day