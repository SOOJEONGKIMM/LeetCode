class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt=idx=0
        for i in nums:
            if i==0:
                idx+=1
                cnt+=idx
            else:
                idx=0
                
        return cnt #Time: O(n), space: O(1), where n = nums.length.