class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        last = 0
        for i in range(len(t)):
            while j < len(s) and s[j] != t[i]:
                j += 1
            if j == len(s):
                return len(t) - i
            j += 1
            last = i + 1
        return len(t) - last