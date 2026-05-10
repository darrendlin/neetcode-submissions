class Solution:
    def canJump(self, nums: List[int]) -> bool:
        highest = 0
        reach = nums[0]
        for i in range(len(nums)-1):
            if i > highest:
                return False
            reach = nums[i] + i
            highest = max(highest, reach)
            print(i, nums[i], highest)
            if highest >= len(nums)-1:
                return True
        return highest >= len(nums)-1