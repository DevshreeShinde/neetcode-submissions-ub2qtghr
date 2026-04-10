class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        ans=[]
        for i in range(len(nums)):
            store[nums[i]] = store.get(nums[i], 0) + 1
        
        # Sort dictionary items by value (frequency) in descending order
        sorted_items = sorted(store.items(), key=lambda x: x[1], reverse=True)
        
        # Take the first k keys from the sorted items
        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans