from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tree_node import TreeNode

def postorderTraversal(self, root:TreeNode) -> list:
    """
    Function taking a root node of type Treenode and traversing
    threw in in postorder while adding the value of each visited
    node to the result list and returning it.
    """
    def postorder_helper(node:TreeNode, result:list) -> None:
        """
        Helper function defining the traversal order in postorder.
        """
        if node:
            postorder_helper(node.left, result)
            postorder_helper(node.right, result)
            result.append(node.val)
    
    result = []
    postorder_helper(root, result)
    return result