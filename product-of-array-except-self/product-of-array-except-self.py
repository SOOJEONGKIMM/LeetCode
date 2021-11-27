class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        tmp=1
        for i in range(len(nums)):
            res.append(tmp)
            tmp*=nums[i]
        res_tmp=[]
        tmp=1
        for i in range(len(nums)-1,-1,-1):
            res_tmp.append(tmp)
            tmp*=nums[i]
        res_tmp.reverse()
        
        for i in range(len(nums)):
            res[i]=res[i]*res_tmp[i]
        
        return res