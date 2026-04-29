class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currmax = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i]=currmax
            currmax=max(tmp,currmax)
        return arr

        