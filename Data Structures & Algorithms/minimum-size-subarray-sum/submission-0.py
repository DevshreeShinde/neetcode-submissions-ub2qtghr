class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        curr = 0
        left = 0
        for i in range(len(nums)):
            curr = curr+nums[i]
            while curr>=target:
                ans = min(ans,i-left+1)
                curr-=nums[left]
                left+=1
        return 0 if ans==float('inf') else ans
        