#TC: O(N^2) SC:O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                curr=nums[i]+nums[left]+nums[right]
                if curr==0:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and (nums[left]==nums[left-1]):
                        left+=1
                    while left<right and (nums[right]==nums[right+1]):
                        right-=1
                elif curr<0 :
                    left+=1
                elif curr>0:
                    right-=1
        return triplets
        
