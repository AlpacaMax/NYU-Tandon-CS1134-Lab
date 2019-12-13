import random
from UnsortedArrayMap import UnsortedArrayMap
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()



class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return (((self.a * hash(key)) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        self.table = make_array(self.N)
        for i in range(self.N):
            self.table[i] = UnsortedArrayMap()
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(self.N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if(new_size > old_size):
            self.n += 1
        if(self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.n -= 1
        if(self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, value) in old:
            self[key] = value
