# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        store = []
        ans = []
        store.append(root)
        while store:
            n = len(store)
            while n:
                curr = store.pop(0)
                if curr.left:
                    store.append(curr.left)
                if curr.right:
                    store.append(curr.right)
                if n==1:
                    ans.append(curr.val)
                n-=1
        return ans