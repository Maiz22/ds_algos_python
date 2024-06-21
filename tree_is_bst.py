from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tree_node import TreeNode

def remove_none_helper(lst) -> list:
    return [x for x in lst if lst is not None]

def is_bst(node:TreeNode):
    """
    Function checking whether a tree is a binary search
    tree. 
    Conditions:
    1) lefts subtrees values are smaller than current nodes values
    2) right subtrees values are bigger than current nodes values
    """
    if node is None:
        return True, None, None

    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)

    is_bst_node = (is_bst_left and is_bst_right and 
                   (max_left is None or max_left < node.val) and 
                   (min_right is None or min_right > node.val))
    
    min_val = min(remove_none_helper(min_left, node.val, min_right))
    max_val = max(remove_none_helper(max_left, node.val, max_right))

    return is_bst_node, min_val, max_val
    