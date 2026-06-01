class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            lenS = len(s)
            output += str(lenS) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        lenS = len(s)
        i = 0
        while i < lenS:
            lenC = ""
            for j in range(i, lenS):
                lenC += s[j]

                if s[j + 1] == "#":
                    num = int(lenC)
                    print(num)
                    output.append(s[j + 2:j + 2 + num])
                    i = j + 2 + num
                    lenC = ""
                    break
        return output
