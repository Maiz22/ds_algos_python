"""
Creating a class representing a tree like structure.
Added some basic methods.
"""

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def height(self) -> int:
        """
        Returns the total height of the TreeNode object.
        """
        if self is None:
            return 0
        height_left_child = TreeNode.height(self.left)
        height_right_child = TreeNode.height(self.right)
        return 1 + max(height_left_child, height_right_child)
    
    def size(self) -> int:
        """
        Returns the total size (amount of nodes) of the 
        Treenode object.
        """
        if self is None:
            return 0
        size_left_child = TreeNode.size(self.left)
        size_right_child = TreeNode.size(self.right)
        return 1 + size_left_child + size_right_child
    

def parse_tuple(data):
    """
    Helper function creating a Tree from a tree tuple:
    """
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


if __name__ == "__main__":
    tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    print(tree.height())
    print(tree.size())
