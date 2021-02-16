#TC: O(N^3) SC:O(1)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                left=j+1
                right=len(nums)-1
                curr=nums[i]+nums[j]
                while left<right:
                    if curr+nums[left]+nums[right]==target:
                        temp=[nums[i],nums[j],nums[left],nums[right]]
                        res.append(temp)
                        while(left<right and nums[left]==temp[2]):
                            left+=1
                        while (left<right and nums[right]==temp[3]):
                            right-=1                 
                    elif curr+nums[left]+nums[right]<target:
                        left+=1
                    elif curr+nums[left]+nums[right]>target:
                        right-=1
                while(j+1<len(nums) and nums[j]==nums[j+1]):
                    j+=1 
                j+=1
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            i+=1
        return res
                    
