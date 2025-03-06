class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        merged_cur = merged[-1]

        for cur in intervals[1:]:
            if cur[0] <= merged_cur[1]:
                merged_cur[1] = max(merged_cur[1], cur[1])
            else:
                merged.append(cur)
                merged_cur = merged[-1]
        
        return merged
