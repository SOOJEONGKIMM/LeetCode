class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        l,r=0,0
        ans=0
        window=defaultdict()
        for r, char in enumerate(s):
            if char in window and l<=window[char]:
                l = window[char]+1
            else:
                ans = max(ans, r-l+1)
            #print(window, l, r)
            window[char] = r
        return ans
