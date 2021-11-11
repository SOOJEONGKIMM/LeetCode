class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start=1
        
        while True:
            total = start
            is_valid = True
            
            for i in nums:
                total += i
                
                if total < 1:
                    is_valid = False
                    break
                    
            if is_valid:
                return start
            else:
                start+=1