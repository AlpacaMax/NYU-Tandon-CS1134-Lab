from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue

def binary_tree_even_sum(root):
    if (root is None):
        return 0
    else:
        result = binary_tree_even_sum(root.left) \
                + binary_tree_even_sum(root.right)
        if (root.data % 2 == 0):
            result += root.data
        return result

def binary_tree_has_val(root, val):
    if (root is None):
        return False
    else:
        return (root.data == val) \
                or (binary_tree_has_val(root.left, val)) \
                or (binary_tree_has_val(root.right, val))

def invert_binary_tree1(root):
    if (root is not None):
        invert_binary_tree1(root.left)
        invert_binary_tree1(root.right)
        root.left, root.right = root.right, root.left

def invert_binary_tree2(root):
    if (root is None):
        return
    line = ArrayQueue()
    line.enqueue(root)
    while (line.is_empty() == False):
        curr_node = line.dequeue()
        curr_node.left, curr_node.right \
            = curr_node.right, curr_node.left
        if (curr_node.left is not None):
            line.enqueue(curr_node.left)
        if (curr_node.right is not None):
            line.enqueue(curr_node.right)

def is_full(root):
    if (root.left is None and root.right is None):
        return True
    elif (root.left is None or root.right is None):
        return False
    else:
        return is_full(root.left) and is_full(root.right)

def is_complete(root):
    if (root is None):
        return True
    
    line = ArrayQueue()
    line.enqueue(root)
    level = 0
    while (line.is_empty() == False):
        if (len(line) != 2**level):
            return False
        
        for i in range(2**level):
            curr_node = line.dequeue()
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)
        
        level += 1
    return True

#For q6, see the preorder_with_stack(self) method in LinkedBinaryTree

def main():
    '''
    Define a normal binary tree
    '''
    r_1 = LinkedBinaryTree.Node(5)
    l_2 = LinkedBinaryTree.Node(4, None, r_1)
    r_2 = LinkedBinaryTree.Node(10)
    r_3 = LinkedBinaryTree.Node(8, None, r_2)
    l_3 = LinkedBinaryTree.Node(6, l_2, r_3)
    l_1 = LinkedBinaryTree.Node(31)
    r_1 = LinkedBinaryTree.Node(49)
    r_2 = LinkedBinaryTree.Node(43, l_1, r_1)
    l_2 = LinkedBinaryTree.Node(17)
    r_3 = LinkedBinaryTree.Node(19, l_2, r_2)
    root = LinkedBinaryTree.Node(11, l_3, r_3)
    bt = LinkedBinaryTree(root)

    '''
    Define a full(proper) binary tree
    '''
    l = LinkedBinaryTree.Node(9)
    r = LinkedBinaryTree.Node(11)
    l = LinkedBinaryTree.Node(1, l, r)
    r = LinkedBinaryTree.Node(4)
    r = LinkedBinaryTree.Node(6, l, r)
    l = LinkedBinaryTree.Node(3)
    root = LinkedBinaryTree.Node(7, l, r)
    full_bt = LinkedBinaryTree(root)

    '''
    Define a complete binary tree
    '''
    l1_1 = LinkedBinaryTree.Node(14)
    r1_1 = LinkedBinaryTree.Node(5)
    l1_2 = LinkedBinaryTree.Node(12)
    r1_2 = LinkedBinaryTree.Node(7)
    l1_3 = LinkedBinaryTree.Node(8)
    r1_3 = LinkedBinaryTree.Node(15)
    l1_4 = LinkedBinaryTree.Node(1)
    r1_4 = LinkedBinaryTree.Node(4)
    l2_1 = LinkedBinaryTree.Node(13, l1_1, r1_1)
    r2_1 = LinkedBinaryTree.Node(9, l1_2, r1_2)
    l2_2 = LinkedBinaryTree.Node(3, l1_3, r1_3)
    r2_2 = LinkedBinaryTree.Node(6, l1_4, r1_4)
    l3 = LinkedBinaryTree.Node(2, l2_1, r2_1)
    r3 = LinkedBinaryTree.Node(11, l2_2, r2_2)
    root = LinkedBinaryTree.Node(10, l3, r3)
    complete_bt = LinkedBinaryTree(root)