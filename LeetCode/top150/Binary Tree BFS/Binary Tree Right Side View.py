from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq = deque([root])
        answer = []
        while dq:
            n = len(dq)
            tmp = []
            for _ in range(n):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            answer.append(tmp)

        return [level[-1] for level in answer]

    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer

        dq = deque()
        dq.append(root)

        while dq:
            length = len(dq)
            for i in range(length):
                node = dq.popleft()
                if i == (length - 1):
                    answer.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return answer
