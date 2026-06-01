class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = dict()

        for n in nums:
            if n not in data:
                data[n] = 1
            else:
                data[n] += 1
        
        sortedData = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
        
        output = []
        for key in sortedData:
            output.append(key)
            if len(output) == k:
                return output