class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a=list(map(str,title.split()))
        b=[]
        for i in a:
            if len(i)>2:
                b.append(i.capitalize())
            else:
                b.append(i.lower())
        return " ".join(b)
        