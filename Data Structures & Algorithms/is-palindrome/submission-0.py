class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            temp += s[i].lower()

        j = len(temp) - 1
        for i in range(len(temp)):    
            if temp[i] != temp[j]:
                return False
            j -= 1

        return True