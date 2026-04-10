class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        ans = []
        for i in range(len(nums)):
            if target-nums[i] in store:
                ans.append(store[target-nums[i]])
                ans.append(i)
                return ans
            store[nums[i]]=i
        return ans

        