class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=list(range(max(nums)+1))
        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        def union(x, y):
            p[find(x)] = p[find(y)]      

        
       
        
        for i in nums:
            for j in range(2, int(math.sqrt(i)+1)):
                if i%j==0:
                    union(i,j)
                    union(i,i//j)
        return collections.Counter([find(i) for i in nums]).most_common(1)[0][1]
        