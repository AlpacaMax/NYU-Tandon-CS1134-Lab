from ArrayList import ArrayList

class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def top(self):
        if(self.is_empty() == True):
            raise Exception("Stack is Empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty() == True):
            raise Exception("Stack is Empty")
        return self.data.pop()

