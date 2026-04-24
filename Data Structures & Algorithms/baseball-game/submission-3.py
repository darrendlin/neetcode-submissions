class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        total = 0
        for op in operations:
            if op == "+":
                i = scores[-1] + scores[-2]
                scores.append(i)
                total += i
            elif op == "D":
                i = scores[-1] * 2
                scores.append(i)
                total += i
            elif op == "C":
                total -= scores.pop()
            else:
                i = int(op)
                scores.append(i)
                total += i

        return total