class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr=[]
        for i in range(left,right+1):
            n=len(str(i))
            count=0
            for j in str(i):
                if int(j)==0:
                    continue
                if i%int(j)==0:
                    count+=1
                else:
                    count=0
            if count==n:
                arr.append(i)
        return arr

        