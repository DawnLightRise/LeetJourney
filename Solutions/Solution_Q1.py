class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, value in enumerate(nums):
            resi = target - value
            if resi in dic:
                return [i, dic[resi]]

            dic[value] = i
