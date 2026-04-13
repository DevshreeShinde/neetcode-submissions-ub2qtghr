class Solution:
    def combosum(self,candidates,target,curr,ans,index):
        if target==0:
            ans.append(curr[:])
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if(candidates[i]>target):
                continue
            curr.append(candidates[i])
            self.combosum(candidates,target-candidates[i],curr,ans,i+1)
            curr.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.combosum(candidates, target, [], ans, 0)
        return ans