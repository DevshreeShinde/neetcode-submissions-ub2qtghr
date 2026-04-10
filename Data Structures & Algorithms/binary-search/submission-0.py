class Solution:
    def binarysearch(self,start,end,nums,target):
        if start > end:
            return -1
        mid=int((start+end)/2)
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            return self.binarysearch(mid+1,end,nums,target)
        else:
            return self.binarysearch(start,mid-1,nums,target)

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end=len(nums)-1
        return self.binarysearch(start,end,nums,target)