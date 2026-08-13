class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # if k == 0:
        #     return [0] * len(code)

        # n = code + code
        # a = []
        # l = len(code)

        # if k > 0:
        #     for i in range(1, l + 1):
        #         a.append(sum(n[i:i + k]))
        # else:
        #     k = -k
        #     for i in range(l):
        #         a.append(sum(n[i + l - k:i + l]))

        # return a
        c=code+code
        r=[]
        n=len(code)
        if k>0:
            for i in range(len(code)):
                r.append(sum(c[i+1:i+1+k]))
        else:
            for i in range(len(code)):
                r.append(sum(c[i + n + k:i + n]))
        return r