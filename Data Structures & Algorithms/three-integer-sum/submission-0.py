class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import collections

        m = collections.defaultdict(set)

        for i in range(len(nums)):
            m[nums[i]].add(i)

        setfset = set()
        res = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                need = 0 - nums[i] - nums[j]
                if need in m:    
                    for k in m[need]:
                        if k != i and k != j:
                            fset = frozenset({nums[i], nums[j], need})
                            if fset not in setfset:
                                setfset.add(fset)
                                res.append([nums[i], nums[j], need])
        return res