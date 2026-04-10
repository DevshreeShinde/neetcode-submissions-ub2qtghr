class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        store = {}
        for st in strs:
            key = "".join(sorted(st)) 
            store[key]=store.get(key,[])+[st]
        for value in store.values():
            ans.append(value)
        return ans