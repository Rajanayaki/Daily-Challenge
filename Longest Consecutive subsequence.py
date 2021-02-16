#TC: O(N) SC:O(N)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=1
        long=0
        for i in nums:
            if i-1 not in dic:
                curr=i
                currcount=1
                while curr+1 in dic:
                    currcount+=1
                    curr+=1
                long=max(currcount,long)
        return long
