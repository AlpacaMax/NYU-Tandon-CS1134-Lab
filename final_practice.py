from DoublyLinkedList import DoublyLinkedList
from ChainingHashTableMap import ChainingHashTableMap
from LinkedBinaryTree import LinkedBinaryTree

def remove_duplicates(lnk_lst):
    record = ChainingHashTableMap()
    cursor = lnk_lst.header.next
    while (cursor is not lnk_lst.trailer):
        if (cursor.data in record):
            node = cursor
            cursor = cursor.next
            lnk_lst.delete_node(node)
        else:
            record[cursor.data] = None
            cursor = cursor.next

def is_size_tree(bin_tree):
    result = is_size_tree_helper(bin_tree.root)
    return result[0]

def is_size_tree_helper(root):
    sub_size = 1
    left = True
    right = True
    if (root.left is not None):
        result = is_size_tree_helper(root.left)
        left = result[0]
        sub_size += result[1]
    if (root.right is not None):
        result = is_size_tree_helper(root.right)
        right = result[0]
        sub_size += result[1]
    
    return (left and right and sub_size == root.data, sub_size)

class ExtendedPartiesQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.name_size_map = ChainingHashTableMap()
    
    def __len__(self):
        return len(self.data)
    
    def enq_party(self, party_name, party_size):
        self.data.add_last(party_name)
        self.name_size_map[party_name] = party_size
    
    def add_to_party(self, party_name, size_to_add):
        if (party_name not in self.name_size_map):
            raise Exception(party_name + " not in ExtendedPartiesQueue")

        self.name_size_map[party_name] += size_to_add
    
    def first_party(self):
        if (len(self) == 0):
            raise Exception("ExtendedPartiesQueue is empty")

        first_party_name = self.data.header.next.data
        return self.name_size_map[first_party_name]
    
    def deq_first_party(self):
        if (len(self) == 0):
            raise Exception("ExtendedPartiesQueue is empty")

        first_party_name = self.data.delete_first()
        first_party_size = self.name_size_map[first_party_name]

        del self.name_size_map[first_party_name]
        return first_party_size

    def __repr__(self):
        return ", ".join("<{}, {}>".format(name, self.name_size_map[name]) for name in self.data)

def level_list(root, level): #Dec, 18, 2017 final q5
    if (root is None):
        return []
    elif (level == 0):
        return [root.data]
    else:
        left_res = level_list(root.left, level - 1)
        right_res = level_list(root.right, level - 1)
        return left_res + right_res

def main():
    l3 = LinkedBinaryTree.Node(1)
    l2 = LinkedBinaryTree.Node(2, l3, None)
    l4 = LinkedBinaryTree.Node(1)
    r4 = LinkedBinaryTree.Node(1)
    l3 = LinkedBinaryTree.Node(3, l4, r4)
    l5 = LinkedBinaryTree.Node(1)
    r5 = LinkedBinaryTree.Node(1)
    r4 = LinkedBinaryTree.Node(3, l5, r5)
    r3 = LinkedBinaryTree.Node(4, None, r4)
    r2 = LinkedBinaryTree.Node(12, l3, r3)
    root = LinkedBinaryTree.Node(11, l2, r2)
    bt = LinkedBinaryTree()
    bt.root = root

    '''
    pq = ExtendedPartiesQueue()
    pq.enq_party("Jeff", 3)
    print(pq)
    pq.enq_party("Mike", 5)
    print(pq)
    pq.enq_party("Nick", 2)
    print(pq)
    pq.deq_first_party()
    print(pq)
    pq.enq_party("Jessica", 4)
    print(pq)
    pq.add_to_party("Nick", 2)
    print(pq)
    pq.deq_first_party()
    print(pq)
    '''

    print(level_list(bt.root, 5))

main()