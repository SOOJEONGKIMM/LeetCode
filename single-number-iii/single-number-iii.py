from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = Counter(nums)
        items = cnt.items()
        
        ans=[]
        for key, val in items:
            if val==1:
                ans.append(key)
                
        return ans 