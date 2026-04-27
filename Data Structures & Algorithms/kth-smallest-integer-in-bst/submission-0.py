# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self,root,ans):
        if root==None:
            return []
        ans.append(root.val)
        self.traverse(root.left,ans)
        self.traverse(root.right,ans)
        return ans
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        ans = self.traverse(root,ans)
        heapq.heapify(ans)
        for i in range(k-1):
            heapq.heappop(ans)
        return heapq.heappop(ans)
        