class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        ones=0
        answer=""
        for right in range(len(s)):
            if s[right]=="1":
                ones+=1
            while ones>k:
                if s[left]=="1":
                    ones-=1
                left+=1
            if ones==k:
                while s[left]=='0':
                    left+=1
                current=s[left:right+1]

                if answer=="" or len(current)<len(answer):
                    answer=current
                elif len(current)==len(answer) and current <answer:
                    answer=current
        return answer