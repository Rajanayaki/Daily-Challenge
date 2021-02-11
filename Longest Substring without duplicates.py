#TC :O(N) SC:O(N+A)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastseen={}
        longest=[0,0]
        start=0
        for i,char in enumerate(s):
            if char in lastseen:
                start=max(start,lastseen[char]+1)
            if longest[1]-longest[0]<i+1-start:
                longest=[start,i+1]
            lastseen[char]=i
        return longest[1]-longest[0]
        
