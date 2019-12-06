from BinarySearchTreeMap import BinarySearchTreeMap
from LinkedBinaryTree import LinkedBinaryTree

def min_max_BST(bst):
    if (bst.is_empty()):
        raise Exception("BinarySearchTreeMap is empty")

    min_node = bst.root
    while (min_node.left is not None):
        min_node = min_node.left
    
    max_node = bst.subtree_max(bst.root)
    return (min_node.item.key, max_node.item.key)

def glt_n(bst, n):
    if (bst.is_empty()):
        raise Exception("BinarySearchTreeMap is empty")

    record = []
    curr_node = bst.root

    while (curr_node is not None):
        record.append(curr_node.item.key)
        if (curr_node.item.key <= n):
            curr_node = curr_node.right
        else:
            curr_node = curr_node.left

    record = sorted(record)
    if (record[0] > n):
        return -1
    elif (record[-1] <= n):
        return record[-1]
    
    for i in range(len(record)):
        if (record[i] > n):
            return record[i - 1]

def compare_BST(bst1, bst2):
    return [key for key in bst1] == [key for key in bst2]

def is_BST(root):
    return is_BST_helper(root)[2]

def is_BST_helper(root):#Notice that this tree here is a LinkedBinaryTree
    if (root.left is None and root.right is None):
        return (root.data, root.data, True)
    elif (root.left and root.right):
        res_left = is_BST_helper(root.left)
        res_right = is_BST_helper(root.right)
        right_gt_left = res_left[1] < res_right[0]
        root_gt_left = root.data > res_left[1]
        root_lt_right = root.data < res_right[0]
        return (res_left[0], res_right[1],
                res_left[2] 
                and res_right[2] 
                and right_gt_left 
                and root_gt_left
                and root_lt_right)
    elif (root.left):
        res_left = is_BST_helper(root.left)
        root_gt_left = root.data > res_left[1]
        return (res_left[0], res_left[1],
                res_left[2] and root_gt_left)
    else:
        res_right = is_BST_helper(root.right)
        root_lt_right = root.data < res_right[0]
        return (res_right[0], res_right[1],
                res_right[2] and root_lt_right)

def lca_BST(bst, node1, node2):
    def lca_BST_helper(bst, curr):
        next1 = curr
        next2 = curr

        if (curr.item.key > node1.item.key):
            next1 = curr.left
        else:
            next1 = curr.right
        
        if (curr.item.key > node2.item.key):
            next2 = curr.left
        else:
            next2 = curr.right
        
        if ((next1 is not next2) or (curr is node1)):#We should also consider the situation when node1 and node2 are the same
            return curr
        else:
            return lca_BST_helper(bst, next1)
    return lca_BST_helper(bst, bst.root)

def lca_BT(bt, node1, node2):
    trace1 = []
    trace2 = []

    curr1 = node1
    while (curr1 is not None):
        trace1.append(curr1)
        curr1 = curr1.parent
    
    curr2 = node2
    while (curr2 is not None):
        trace2.append(curr2)
        curr2 = curr2.parent
    
    for i in range(-1, -min(len(trace1), len(trace2)) - 1, -1):
        if (trace1[i] is not trace2[i]):
            return trace1[i+1]

def main():
    bst = BinarySearchTreeMap()
    bst.insert(2)
    bst.insert(12)
    bst.insert(1)
    bst.insert(3)
    bst.insert(9)
    bst.insert(21)
    bst.insert(19)
    bst.insert(25)

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

    node1 = bst.root.right
    node2 = bst.root.right

    print(lca_BST(bst, node1, node2).item.key)