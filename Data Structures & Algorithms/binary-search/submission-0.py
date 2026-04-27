class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin(s: int, e: int):
            if s > e:
                return -1
            m = (s + e) // 2

            

            if nums[m] == target:
                return m
            elif nums[m] > target:
                return bin(s, m-1)
            else:
                return bin(m+1, e)
        
        return bin(0, len(nums)-1)