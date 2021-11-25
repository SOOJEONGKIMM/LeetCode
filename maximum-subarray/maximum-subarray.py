class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [i for i in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            

        return max(dp)