class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        m = len(digits)

        for cur in range(m - 1, 0, -1):
            prev = cur - 1
            if digits[cur] < digits[prev]:
                digits[prev] -= 1
                digits[cur:] = [9] * (m - cur)

        return int("".join(str(x) for x in digits))
