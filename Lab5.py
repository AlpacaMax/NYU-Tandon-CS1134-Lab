import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if ind < 0:
            ind += self.n

        if(not(0 <= ind <= self.n - 1)):
            raise IndexError("invalid index")
        return self.data_arr[ind]

    def __setitem__(self, ind, value):
        if ind < 0:
            ind += self.n

        if (not (0 <= ind <= self.n - 1)):
            raise IndexError("invalid index")
        self.data_arr[ind] = value

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def __repr__(self):
        if len(self) == 0:
            return '[]'

        strRepr = '['
        for i in range(len(self) - 1):
            strRepr += str(self[i]) + ', '
        strRepr += str(self[len(self) - 1]) + ']'
        
        return strRepr
    
    def __add__(self, other):
        result = ArrayList()
        for elem in self:
            result.append(elem)
        
        for elem in other:
            result.append(elem)
        
        return result
    
    def __iadd__(self, other):
        for i in other:
            self.append(i)
        
        return self
    
    def __mul__(self, k):
        result = ArrayList()

        for i in range(k):
            for j in self:
                result.append(j)
        
        return result
    
    def __rmul__(self, k):
        return self.__mul__(k)