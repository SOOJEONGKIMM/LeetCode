class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        stair=0
        i=0
        while 1:
            i+=1
            stair+=i
            if stair >= n:
                row=i
                break
        if stair>n:
            row-=1
        return row
        
