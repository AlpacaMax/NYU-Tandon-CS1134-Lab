import Lab1

def twos_powers(n):
    for i in range(n):
        yield 2**i

def reverse_twos_powers(n):
    for i in range(n):
        yield 0.5**i

'''
n = int(input('Enter a positive integer, n: '))
for i in range(1, n+1):
    total = sum([num for num in twos_powers(i)])
    print(total)

n = int(input('Enter a positive integer, n: '))
for i in range(1, n+1):
    total = sum([num for num in reverse_twos_powers(i)])
    print(total)
'''

class UnsignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str
    
    def __add__(self, other):
        if not isinstance(other, UnsignedBinaryInteger):
            raise ValueError("Must be usginedBinaryInteger type")

        result = UnsignedBinaryInteger(Lab1.add_binary(self.data, other.data))
        return result
    
    def decimal(self):
        return sum([2**i for i in range(len(self.data)) if self.data[-(i+1)] == '1'])
    
    def __lt__(self, other):
        if not isinstance(other, UnsignedBinaryInteger):
            raise ValueError("Must be unsignedBinaryInteger type")

        if self.decimal() < other.decimal():
            return True
        else:
            return False
    
    def __gt__(self, other):
        if not isinstance(other, UnsignedBinaryInteger):
            raise ValueError("Must be unsignedBinaryInteger type")

        if self.decimal() > other.decimal():
            return True
        else:
            return False
    
    def __eq__(self, other):
        if not isinstance(other, UnsignedBinaryInteger):
            raise ValueError("Must be unsignedBinaryInteger type")

        if self.data == other.data:
            return True
        else:
            return False
    
    def is_twos_power(self):
        for i in range(1, len(self.data)):
            if self.data[i] == '1':
                return False
        return True
    
    def largest_twos_power(self):
        return 2**(len(self.data) - 1)
    
    def __repr__(self):
        return '0b' + self.data
    
    def __or__(self, other):
        if not isinstance(other, UnsignedBinaryInteger):
            raise ValueError("Must be unsignedBinaryInteger type")

        num1 = self.data
        num2 = other.data
        result = ''

        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = '0'*(len(num2) - len(num1)) + num1

        for i in range(len(num1)):
            if num1[i] == '1' or num2[i] == '1':
                result += '1'
            else:
                result += '0'
        
        while result[0] == '0' and len(result) > 1:
            result = result[1:]
        
        return UnsignedBinaryInteger(result)
    
    def __and__(self, other):
        if not isinstance(other, UnsignedBinaryInteger):
            raise ValueError("Must be unsignedBinaryInteger type")

        num1 = self.data
        num2 = other.data
        result = ''

        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = '0'*(len(num2) - len(num1)) + num1
        
        for i in range(len(num1)):
            if num1[i] == '1' and num2[i] == '1':
                result += '1'
            else:
                result += '0'
        
        while result[0] == '0' and len(result) > 1:
            result = result[1:]
        
        return UnsignedBinaryInteger(result)

b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')
print("\nTesting b1: ", b1, "b2: ", b2)
b3 = b1 | b2
b4 = b1 & b2
print(b1, "|", b2, "=", b3) #0b100
print(b1, "&", b2, "=", b4)
b1 = UnsignedBinaryInteger('1010')
b2 = UnsignedBinaryInteger('1001')
print("\nTesting b1: ", b1, "b2: ", b2)
b3 = b1 | b2
b4 = b1 & b2
print(b1, "|", b2, "=", b3)
print(b1, "&", b2, "=", b4)