class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()

        for i, n in enumerate(nums):
            data[n] = i
        
        
        for i, n in enumerate(nums):
            if target - n in data and data[target - n] != i:
                return [i, data[target - n]]