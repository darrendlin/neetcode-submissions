# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(left: List[Pair], right: List[Pair]) -> List[Pair]:
            l = 0
            r = 0
            ret = []
            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    ret.append(left[l])
                    l += 1
                else:
                    ret.append(right[r])
                    r += 1
            if l == len(left):
                for i in range(r, len(right)):
                    ret.append(right[i])
            elif r == len(right):
                for i in range(l, len(left)):
                    ret.append(left[i])
            return ret

        print("len = ", len(pairs))
        if len(pairs) <= 1:
            return pairs

        m = len(pairs)//2
        print("middle = ", m)
        print()
        l = self.mergeSort(pairs[:m])
        r = self.mergeSort(pairs[m:])

        merged = merge(l, r)

        return merged