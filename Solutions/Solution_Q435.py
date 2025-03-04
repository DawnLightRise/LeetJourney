class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        current_end = -inf

        for start, end in intervals:
            if start >= current_end:
                current_end = end
            else:
                count += 1

        return count
