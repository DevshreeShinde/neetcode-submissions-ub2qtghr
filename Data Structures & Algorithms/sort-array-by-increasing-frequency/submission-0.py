class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        seen={}
        for i in range(len(nums)):
            seen[nums[i]]=seen.get(nums[i],0)+1
        sorted_seen = dict(sorted(seen.items(), key=lambda x: (x[1], -x[0])))
        ans = []
        for key,values in sorted_seen.items():
            for i in range(values):
                ans.append(key)
        return ans
        