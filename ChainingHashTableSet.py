import random
from DoublyLinkedList import DoublyLinkedList
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ChainingHashTableSet:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.set1 = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return (((self.set1 * hash(key)) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        self.table = make_array(self.N)
        for i in range(self.N):
            self.table[i] = DoublyLinkedList()
        self.n = 0
        self.hash_function = ChainingHashTableSet.MADHashFunction(self.N)

    def add(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]

        for elem in curr_bucket:
            if (elem == key):
                return
        curr_bucket.add_last(key)

        self.n += 1
        if(self.n > self.N):
            self.rehash(2 * self.N)

    def remove(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        
        cursor =  curr_bucket.header.next
        has_key = False
        while (cursor is not curr_bucket.trailer):
            if (cursor.data == key):
                curr_bucket.delete_node(cursor)
                self.n -= 1
                has_key = True
                break

        if (not has_key):
            raise KeyError("Key doesn't exist")
        if(self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key
    
    def __contains__(self, key):
        for elem in self:
            if (elem == key):
                return True
        return False

    def rehash(self, new_size):
        old = [key for key in self]
        self.__init__(new_size)
        for key in old:
            self.add(key)
    
    def intersection(self, other):
        inter = ChainingHashTableSet()
        for key in self:
            if (key in other):
                inter.add(key)
        return inter
    
    def __and__(self, other):
        return self.intersection(other)
    
    def union(self, other):
        union = ChainingHashTableSet()

        for key in self:
            union.add(key)
        for key in other:
            union.add(key)
        
        return union
    
    def __or__(self, other):
        return self.union(other)
    
    def difference(self, other):
        diff = ChainingHashTableSet()
        for key in self:
            if (key not in other):
                diff.add(key)
        return diff
    
    def __sub__(self, other):
        return self.difference(other)

def print_hash_table(hashset):
    print('{' + ', '.join([str(key) for key in hashset]) + '}')

def main():
    set1 = ChainingHashTableSet()
    set1.add(1)
    set1.add(2)
    set1.add(3)
    set1.add("apple")
    set1.add("banana")

    set2 = ChainingHashTableSet()
    set2.add(1)
    set2.add(3)
    set2.add("orange")

    print_hash_table(set2 - set1)
main()