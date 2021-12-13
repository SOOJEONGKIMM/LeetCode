class Solution:
    def maxPower(self, s: str) -> int:
        cnt = 0
        prev = None
        backupcnt=0
        for i in s:
            if i == prev:
                cnt+=1
            else:
                prev = i
                cnt=1
            backupcnt = max(cnt, backupcnt)
        return backupcnt