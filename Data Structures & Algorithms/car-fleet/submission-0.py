class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = 0

        for i in range(len(position)):
            time = ((target - position[i]) / speed[i])
            cars.append([position[i], time])
        
        cars.sort(reverse=True, key=lambda x: x[0])

        slowest_time = 0

        for pos, time in cars:
            if time > slowest_time:
                fleets += 1
                slowest_time = time
            
        return fleets
            





            