import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(numbers):
            m[num] = i
        
        for i, num in enumerate(numbers):
            right = bisect.bisect_left(numbers, target-num, lo=i+1)
            if target - num in m and m[target-num] == right:
                return [i+1, right+1]
            left = bisect.bisect_left(numbers, target-num, hi=i)
            if target - num in m and m[target-num] == left:
                return [left+1, i+1]
        return [0, 0]