import ctypes
from DoublyLinkedList import DoublyLinkedList
from ArrayStack import ArrayStack

def make_array(n):
    return (n * ctypes.py_object)()

class DLLLeakyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = DoublyLinkedList()
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return self.data.is_empty()
    
    def push(self, e):
        self.data.add_first(e)
        if (len(self) > self.max_size):
            self.data.delete_last()
    
    def pop(self):
        if (self.is_empty()):
            raise Exception("Leaky Stack is empty")
        
        return self.data.delete_first()
    
    def top(self):
        if (self.is_empty()):
            raise Exception("Leaky Stack is empty")

        return self.data.delete_first()

class ArrayLeakyStack:
    def __init__(self, max_size):
        self.data = make_array(max_size)
        self.size = 0
        self.SP = None  #Stack Pointer
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return (len(self) == 0)
    
    def push(self, e):
        if (len(self) == len(self.data)):
            baseIndex = (self.SP - self.size + 1) % len(self.data)
            if (baseIndex < 0):
                baseIndex += len(self.data)
            self.data[baseIndex] = None
            self.size -= 1

        if (self.is_empty()):
            self.data[0] = e
            self.SP = 0
            self.size += 1
        else:
            new_SP = (self.SP + 1) % len(self.data)
            self.data[new_SP] = e
            self.size += 1
            self.SP = new_SP
    
    def pop(self):
        if (self.is_empty()):
            raise Exception("Leaky Stack is empty")
        
        new_SP = (self.SP - 1) % len(self.data)
        if (new_SP < 0):
            new_SP += len(self.data)
        
        val = self.data[self.SP]
        self.data[self.SP] = None
        self.size -= 1
        self.SP = new_SP

        if (self.is_empty()):
            self.SP = None
        
        return val

    def top(self):
        if (self.is_empty()):
            raise Exception("Leaky Stack is empty")

        return self.data[self.SP]

class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
        
        def disconnect(self):
            self.data = None
            self.next = None
    
    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return (len(self) == 0)
    
    def add_after(self, node, val):
        new_node = SinglyLinkedList.Node(val, next=node.next)
        node.next = new_node
        self.size += 1
    
    def add_before(self, node, val):
        new_node = SinglyLinkedList.Node(val, next=node)
        cursor = self.header
        while (cursor.next is not node):
            cursor = cursor.next
        
        cursor.next = new_node
        self.size += 1
    
    def add_first(self, val):
        self.add_after(self.header, val)
    
    def add_last(self, val):
        last_node = self.header
        while (last_node.next is not None):
            last_node = last_node.next
        self.add_after(last_node, val)
    
    def delete_node(self, node):
        val = node.data
        prev_node = self.header
        while (prev_node.next is not node):
            prev_node = prev_node.next
        prev_node.next = node.next
        node.disconnect()
        self.size -= 1
        return val
    
    def delete_first(self):
        return self.delete_node(self.header.next)
    
    def delete_last(self):
        last_node = self.header.next
        while (last_node.next is not None):
            last_node = last_node.next
        return self.delete_node(last_node)
    
    def __iter__(self):
        cursor = self.header.next
        while (cursor is not None):
            yield cursor.data
            cursor = cursor.next
    
    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"

class Integer:
    def __init__(self, num_str):
        self.number = SinglyLinkedList()
        for digit in num_str:
            self.number.add_last(int(digit))
    
    def __iadd__(self, other):
        selfStack = ArrayStack()
        otherStack = ArrayStack()
        result = Integer("")

        for elem in self.number:
            selfStack.push(elem)
        for i in range(len(self.number) - len(other.number)):
            otherStack.push(0)
        for elem in other.number:
            otherStack.push(elem)

        hold = 0
        for i in range(len(otherStack)):
            resultDigit = str((selfStack.pop() + otherStack.pop() + hold))

            if (len(resultDigit) == 2):
                hold = int(resultDigit[0])
                result.number.add_first(int(resultDigit[1]))
            else:
                hold = 0
                result.number.add_first(int(resultDigit))
        
        result.number.add_first(hold)
        
        while (result.number.header.next.data == 0 and len(result.number) > 1):
            result.number.delete_first()
        return result

    def __repr__(self):
        result = ""
        for digit in self.number:
            result += str(digit)
        return result

def reverse_dll_by_data(dll):
    start = dll.header.next
    end = dll.trailer.prev
    while (start is not dll.trailer \
        and end is not dll.header \
        and start is not end \
        and start.prev is not end):

        start.data, end.data = end.data, start.data
        start = start.next
        end = end.prev

def reverse_dll_by_node(dll):
    start = dll.header.next
    end = dll.trailer.prev
    while (start is not dll.trailer \
        and end is not dll.header \
        and start is not end \
        and start.prev is not end):
        if (start.next is end):
            start_prev = start.prev
            end_next = end.next
            start, end = end, start

            start_prev.next = start
            end_next.prev = end
            
            start.prev = start_prev
            start.next = end
            end.prev = start
            end.next = end_next
        else:
            start_prev = start.prev
            start_next = start.next
            end_prev = end.prev
            end_next = end.next
            start.next = end_next
            start.prev = end_prev
            end.next = start_next
            end.prev = start_prev
        
            start, end = end, start

            start.prev.next = start
            start.next.prev = start
            end.prev.next = end
            end.next.prev = end

        start = start.next
        end = end.prev