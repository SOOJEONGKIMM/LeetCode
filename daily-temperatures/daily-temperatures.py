class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        ans = [0]*n
        stack=[]
        
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_day = stack.pop()
                ans[prev_day] = cur_day - prev_day
                
            stack.append(cur_day)
            
        return ans