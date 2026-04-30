class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        record = []  # pairs of (temp, index)
        out = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(record) > 0 and record[-1][0] < temperatures[i]:
                popped = record.pop()
                out[popped[1]] = i - popped[1]

            record.append((temperatures[i], i))

        return out