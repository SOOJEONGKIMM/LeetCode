class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        print(sum(piles))
        left = 1
        right = max(piles)
        
        def can_eat_all_bananas(speed):
            time = 0
            for p in piles:
                time += (p + speed -1) // speed
           
            if time <= h:
                return True
            else:
                return False
            
        
        #binary search
        while left < right:
            mid = (left + right) //2 
            if can_eat_all_bananas(mid):
                right = mid
            else:
                left = mid+1
        
        return left
        