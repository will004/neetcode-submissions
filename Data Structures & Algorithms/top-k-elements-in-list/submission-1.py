class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dataCount = dict()
        for n in nums:
            if n not in dataCount:
                dataCount[n] = 1
            else:
                dataCount[n] += 1
        
        data = [[] for i in range(len(nums) + 1)]
        
        for key in dataCount:
            count = dataCount[key]
            data[count].append(key)
        
        output = []
        for idx in range(len(data) - 1, -1, -1):
            if len(output) == k:
                return output
            
            for val in data[idx]:
                output.append(val)