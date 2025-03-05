class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_last_index = {}
        for index, char in enumerate(s):
            char_last_index[char] = index

        res = []
        start, end = 0, 0

        for index, char in enumerate(s):
            end = max(end, char_last_index[char])
            if index == end:
                next_start = index + 1
                res.append(next_start - start)
                start = next_start

        return res
