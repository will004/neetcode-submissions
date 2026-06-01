class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for n in nums:
            frequency[n] += 1
        
        arr = [[] for _ in range(len(nums) + 1)]

        for key in frequency:
            val = frequency[key]
            arr[val].append(key)

        output = list()

        for i in range(len(arr) - 1, -1, -1):
            if not arr[i]:
                continue
            
            for e in arr[i]:
                output.append(e)
                if len(output) >= k:
                    return output

        return output