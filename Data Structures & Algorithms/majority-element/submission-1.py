class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # store = {}
        # for num in nums:
        #     store[num]=store.get(num,0)+1
        #     if store[num]>len(nums)//2:
        #         return num
        # return -1
        candidate = None
        count = 0
        for num in nums:
            if count==0:
                candidate = num
            if num==candidate:
                count+=1
            else:
                count-=1
        return candidate
