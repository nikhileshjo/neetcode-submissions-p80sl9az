class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        curr_fleet = None
        fleet_cnt = 0
        ind = sorted(range(len(position)), key = position.__getitem__, reverse = True)

        for i in ind:
            t = (target - position[i])/ speed[i]

            if curr_fleet and curr_fleet >= t:
                continue
            else:
                curr_fleet = t
                fleet_cnt += 1
        
        return fleet_cnt