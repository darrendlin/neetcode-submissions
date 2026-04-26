class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0]
        i = 0
        while i <= max_reach:
            print(i, max_reach)
            reach = i + nums[i]
            max_reach = max(max_reach, reach)
            print(i, max_reach)
            print()
            if max_reach >= len(nums)-1:
                return True
            i += 1
        return False
            