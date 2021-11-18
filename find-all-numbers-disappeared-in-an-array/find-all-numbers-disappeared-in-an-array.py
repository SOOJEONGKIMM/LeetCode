class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)
        nums.sort()
     
        res=list(set(range(1,length+1)) - set(nums)) 
            
            
        return res
                    