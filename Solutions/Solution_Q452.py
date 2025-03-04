class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 0
        current_end = -inf # For Initialization only
        # To achieve optimality, the arrow needs to be placed at the end of an interval.
        for start, end in points:
            if start > current_end:
                arrows += 1
                current_end = end

        return arrows
