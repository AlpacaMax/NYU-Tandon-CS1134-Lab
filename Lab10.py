from DoublyLinkedList import DoublyLinkedList
from ArrayStack import ArrayStack

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self.data.add_first(e)
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.data.header.next.data

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        val = self.data.header.next.data
        self.data.delete_first()
        return val

class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.add_last(e)
        if (len(self) == 1):
            self.mid = self.data.header.next
        elif len(self) % 2 == 1:
            self.mid = self.mid.next

    def top(self):
        if self.is_empty():
            raise Exception("Midstack is empty")
            
        return self.data.last.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception("Midstack is empty")

        val = self.data.delete_last()
        if len(self) == 0:
            self.mid = None
        elif len(self) % 2 == 0:
            self.mid = self.mid.prev
        
        return val
    
    def mid_push(self, e):
        if (self.is_empty()):
            raise Exception("Midstack is empty")
        elif len(self) % 2 == 0:
            self.data.add_after(self.mid, e)
            self.mid = self.mid.next
        else:
            self.data.add_before(self.mid, e)
            self.mid = self.mid.prev

#Answer of Question 2 is in the DoublyLinkedList.py

def flatten_dll_recursive(dll):
    result = DoublyLinkedList()
    for elem in dll:
        if isinstance(elem, DoublyLinkedList):
            rest = flatten_dll_recursive(elem)
            for num in rest:
                result.add_last(num)
        else:
            result.add_last(elem)
    return result

def flatten_dll(dll):
    result = DoublyLinkedList()
    temp = ArrayStack()
    for elem in dll:
        temp.push(elem)
    
    while not temp.is_empty():
        elem = temp.pop()
        if isinstance(elem, DoublyLinkedList):
            for sub_elem in elem:
                temp.push(sub_elem)
        else:
            result.add_first(elem)
    return result

def main():
    a = DoublyLinkedList()
    a.add_last(1)
    a.add_last(2)
    b = DoublyLinkedList()
    b.add_last(3)
    b.add_last(4)
    c = DoublyLinkedList()
    c.add_last(5)
    c.add_last(6)
    b.add_last(c)
    a.add_last(b)
    a.add_last(7)
    print(flatten_dll(a))