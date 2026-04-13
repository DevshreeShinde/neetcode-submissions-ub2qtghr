class Solution:
    def permutation(self,curr,ans,nums,index):
        if index==len(nums):
            ans.append(nums[:])
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            self.permutation(curr,ans,nums,index+1)
            nums[index],nums[i]=nums[i],nums[index]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        self.permutation(curr,ans,nums,0)
        return ans
        