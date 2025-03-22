class Solution(object):
    def canJump(self, nums):
        maxReach = 0
        n = len(nums)       
        for i in range(n):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= n - 1:
                return True       
        return maxReach >= n - 1