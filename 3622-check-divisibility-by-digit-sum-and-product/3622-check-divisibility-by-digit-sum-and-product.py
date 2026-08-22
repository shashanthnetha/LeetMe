class Solution:
    def checkDivisibility(self, n: int) -> bool:    
        sum=0
        product=1
        o=n
        while n>0:
            sum+=n%10
            product*=n%10
            n=n//10
        return o%(sum+product)==0
