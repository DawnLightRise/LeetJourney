class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            h = min(height[i], height[j])
            area = h * (j - i)
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return max_area
