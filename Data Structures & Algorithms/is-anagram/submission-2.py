class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data_s, data_t = dict(), dict()

        for i in range(len(s)):
            if s[i] in data_s:
                data_s[s[i]] += 1
            else:
                data_s[s[i]] = 1
            
            if t[i] in data_t:
                data_t[t[i]] += 1
            else:
                data_t[t[i]] = 1
        
        return data_s == data_t