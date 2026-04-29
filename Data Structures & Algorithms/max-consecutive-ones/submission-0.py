class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        currones = 0
        for num in nums:
            if num==1:
                currones+=1
                maxones=max(maxones,currones)
            else:
                currones=0
        return maxones

        