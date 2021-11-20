from collections import Counter
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        res=Counter(nums)
        
        for key, value in res.items():
            if value==1:
                cnt=key 
    
        return cnt