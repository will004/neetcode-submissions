class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = dict()

        for s in strs:
            key = ''.join(sorted(s))
            if key not in data:
                data[key] = []
                
            data[key].append(s)
        
        return [data[e] for e in data]