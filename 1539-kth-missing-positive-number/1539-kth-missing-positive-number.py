class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        full_ = list(range(1,max_num))
        cnt,i=0,0
        
        while True:
            i+=1
            if i not in arr and i <= max_num:
                cnt+=1
                if cnt==k:
                    return i
            elif i > max_num:
                cnt+=1
                if cnt==k:
                    break
        return i
      
                
                
                
                
            
        