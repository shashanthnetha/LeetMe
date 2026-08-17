class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        a = []

        for i in image:
            x = []

            for j in i[::-1]:
                if j == 0:
                    x.append(1)
                else:
                    x.append(0)

            a.append(x)

        return a
        
        