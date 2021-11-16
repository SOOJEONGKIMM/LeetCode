class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def search(m,n,k,mid):
            cnt=0
            for i in range(1,m+1):
                cnt+=min(mid//i,n)
                if cnt>=k:
                    return cnt
            return cnt
        
        left=1
        right=m*n
        while left<=right:
            mid = left + (right-left)//2
            if search(m,n,k,mid)>=k:
                right=mid-1
            else:
                left=mid+1
        return left
        
    