import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = pos = neg = nums[0]
        for n in nums[1:]:
            if n < 0:
                pos, neg = n*neg, min(n*pos, n)
            else:
                pos, neg = max(n*pos, n), n*neg
            ans = max(ans, pos)
        return ans