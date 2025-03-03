class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        total_tank = 0
        curr_tank = 0
        start_station = 0

        for station in range(n):
            total_tank += gas[station] - cost[station]
            curr_tank += gas[station] - cost[station]

            if curr_tank < 0:
                start_station = station + 1
                curr_tank = 0

        return start_station if total_tank >= 0 and start_station < n else -1
