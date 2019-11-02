import ctypes  # provides low-level arrays
from ArrayQueue import ArrayQueue
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue_last(self, elem):
        if(self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data_arr)
            self.data_arr[back_ind] = elem
            self.num_of_elems += 1

    def enqueue_first(self, elem):
        if(self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            self.front_ind -= 1

            if self.front_ind < 0:
                self.front_ind = len(self.data_arr) + self.front_ind

            self.data_arr[self.front_ind] = elem
            self.num_of_elems += 1

    def dequeue_first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayDeque.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val
    
    def dequeue_last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data_arr[(self.front_ind + self.num_of_elems - 1) % len(self.data_arr)]
        self.data_arr[(self.front_ind + self.num_of_elems - 1) % len(self.data_arr)] = None
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayDeque.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]
    
    def last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % len(self.data_arr)
        return self.data_arr[back_ind]

    def resize(self, new_capacity):
        new_arr = make_array(new_capacity)
        old_arr = self.data_arr
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_arr[new_ind] = old_arr[old_ind]
            old_ind = (old_ind + 1) % len(old_arr)
        self.data_arr = new_arr
        self.front_ind = 0

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, e):
        if not isinstance(e, (int, float)):
            raise TypeError("Item must be int or float type!")

        self.data.enqueue(e)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("MeanQueue is empty!")

        return self.data.dequeue()
    
    def first(self):
        if self.is_empty():
            raise Exception("MeanQueue is empty!")

        return self.data.first()

    def sum(self):
        total = 0
        for i in range(len(self)):
            total += self.data.first()
            self.data.enqueue(self.data.dequeue())
        return total
    
    def mean(self):
        return self.sum() / len(self)

def n_bonacci(n, k):
    numQueue = ArrayQueue()
    numOfVals = 0
    for i in range(n):
        if numOfVals == k:
            return
        numQueue.enqueue(1)
        numOfVals += 1
        yield 1

    while numOfVals < k:
        nextVal = 0
        for i in range(len(numQueue)):
            nextVal += numQueue.first()
            numQueue.enqueue(numQueue.dequeue())
        numQueue.dequeue()
        numQueue.enqueue(nextVal)
        yield nextVal
        numOfVals += 1

class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self.data.enqueue(e)
    
    def pop(self):
        for i in range(len(self) - 1):
            self.data.enqueue(self.data.dequeue())
        return self.data.dequeue()
    
    def top(self):
        for i in range(len(self) - 1):
            self.data.enqueue(self.data.dequeue())
        val = self.data.first()
        self.data.enqueue(self.data.dequeue())
        return val
