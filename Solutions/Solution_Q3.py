class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        maxNum = 0
        i = 0
        for j, char in enumerate(s):
            if char in hashmap and hashmap[char] >= i:
                i = hashmap[char] + 1

            maxNum = max(maxNum, j - i + 1)
            hashmap[char] = j

        return maxNum