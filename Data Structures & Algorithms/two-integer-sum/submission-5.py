class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()
        for idx, e in enumerate(nums):
            diff = target - e
            if diff in data and data.get(diff, -1) != idx:
                return [data.get(diff), idx]
                
            if e not in data:
                data[e] = idx

        return []