class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        a={}
        b=-1
        min_distance=float('inf')
        for i in range(len(drones)):
            x=drones[i][0]
            y=drones[i][1]
            ran=drones[i][2]
            dis = abs(x - target[0]) + abs(y - target[1])
            if dis<=ran:
                if dis<min_distance:
                    min_distance=dis
                    b=i
        return b

            
            
        
        