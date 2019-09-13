class Polynomial:
    def __init__(self, coefficients = [0]):
        self.coef = coefficients
    
    def __add__(self, other):
        if not isinstance(other, Polynomial):
            raise ValueError("Must be Polynomial")

        if len(self.coef) < len(other.coef):
            self.coef += [0] * (len(other.coef)-len(self.coef))
        elif len(self.coef) > len(other.coef):
            other.coef += [0] * (len(self.coef)-len(other.coef))
        
        result = Polynomial([0] * len(self.coef))
        for i in range(len(self.coef)):
            result.coef[i] = self.coef[i] + other.coef[i]
    
        return result
    
    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            raise ValueError("Must be Polynomial")

        temp = [0] * (len(self.coef) * len(other.coef))
        for i in range(len(self.coef)):
            for j in range(len(other.coef)):
                newPower = i+j
                newCoef = self.coef[i] * other.coef[j]
                temp[newPower] += newCoef
        
        while temp[-1] == 0:
            del temp[-1]
        
        result = Polynomial(temp)
        return result

    def __call__(self, value):
        if not isinstance(value, int):
            raise ValueError("The parameter must be an Integer")

        result = 0
        for i in range(len(self.coef)):
            result += self.coef[i] * (value**i)
        
        return result
    
    def __repr__(self):
        factors = []
        for i in range(len(self.coef) - 1, -1, -1):
            factor = str(self.coef[i]) + 'x^' + str(i)
            factors.append(factor)
        
        return ' + '.join(factors)
    
    def derive(self):
        for i in range(len(self.coef)):
            self.coef[i] *= i
        del self.coef[0]

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Must be Complex")

        result = Complex(self.a + other.a, self.b + other.b)
        return result
    
    def __sub__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Must be Complex")

        result = Complex(self.a - other.a, self.b - other.b)
        return result
    
    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Must be Complex")

        result = Complex(0,0)
        result.a = self.a * other.a - self.b * other.b
        result.b = self.a * other.b + self.b * other.a

        return result
    
    def __str__(self):
        note = ' + '
        if self.b < 0:
            note = ' - '
        
        text = str(self.a) + note + str(abs(self.b)) + 'i'
        return text