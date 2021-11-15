class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans=[]
        max_ind=0
        divcnt=[0 for i in range(len(nums))]
        prev=[-1 for i in range(len(nums))]
        nums.sort()
        idx=-1
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0:
                    if divcnt[i] < divcnt[j]+1 :
                        divcnt[i]=divcnt[j]+1
                        prev[i]=j
                    
                        if divcnt[max_ind] < divcnt[i]:
                            max_ind = i
                            idx=i
        if max_ind==0:
            return [nums[0]]
        while idx!=-1:
            ans.append(nums[idx])
            idx=prev[idx]
       
        return ans