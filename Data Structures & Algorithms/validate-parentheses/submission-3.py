class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        m = {'(': ')', '{': '}', '[': ']'}
        for b in s:
            if b in "({[":
                brackets.append(m[b])
            elif len(brackets) == 0 or brackets.pop() != b:
                return False
        return len(brackets) == 0