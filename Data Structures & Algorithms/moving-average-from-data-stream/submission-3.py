from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.history = deque(maxlen=size)
        self.cur_total = 0

    def next(self, val: int) -> float:
        if len(self.history) == self.history.maxlen:
            self.cur_total -= self.history.popleft()
        self.history.append(val)
        self.cur_total += val
        return self.cur_total / len(self.history)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
