class Solution:

    def subsets(self,nums,curr,ans,index):
        ans.append(curr[:])
        for i in range(index,len(nums)):
            if i>index and nums[i-1]==nums[i]:
                continue
            curr.append(nums[i])
            self.subsets(nums,curr,ans,i+1)
            curr.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr=[]
        ans=[]
        self.subsets(nums,curr,ans,0)
        return ans