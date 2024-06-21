from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tree_node import TreeNode

def preorder_traversal(root:TreeNode) -> list:
    """
    Function taking a root node of type Treenode and traversing
    threw in in preorder while adding the value of each visited
    node to the result list and returning it.
    """

    def preorder_helper(node:TreeNode, result:list) -> None:
        """
        Preorder helper defining the traveral order.
        """
        if node:
            result.append(node.val)
            preorder_helper(node.left, result)
            preorder_helper(node.right, result)

    result = []
    preorder_helper(root, result)
    return result