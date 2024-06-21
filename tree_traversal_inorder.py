from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tree_node import TreeNode


def inorderTraversal(root:TreeNode) -> list:
    """
    Function taking a root node of type Treenode and traversing
    threw in in order while adding the value of each visited
    node to the result list and returning it.
    """

    def inorder_helper(node:TreeNode, result:list) -> None:
        """
        Helper function defining order of the inorder traversal.
        """
        if node:
            inorder_helper(node.left, result)
            result.append(node.val)
            inorder_helper(node.right, result)
    result = []
    inorder_helper(root, result)
    return result