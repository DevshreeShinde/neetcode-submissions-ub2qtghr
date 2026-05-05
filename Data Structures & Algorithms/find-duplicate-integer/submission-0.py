class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check={}
        for num in nums:
            check[num]=check.get(num,0)+1
        for key,value in check.items():
            if value>1:
                return key
        return -1        