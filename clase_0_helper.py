def suma(a,b):
    salida = a+b
    return salida

if __name__ == '__main__':
    a = 4
    b = 5
    print(a+b)

def function(a,b,c=50, d='default'):
    if isinstance(a, str) and isinstance(b,str):
        print(a + b + d)
    else:
        print(a+b+c)
    return d     

class ComplexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def print(self):
        print(f'El número complejo es {self.real}+{self.imag}i')
    def set_real(self, real):
        self.real = real
    def set_imag(self, imag):
        self.imag = imag
    def suma(self, complex_number):
        self.real+=complex_number.real
        self.imag+=complex_number.imag
    def __add__(self, complex_number):# Overloading
        output = ComplexNumbers(
            self.real+complex_number.real,
            self.imag+complex_number.imag)
        return output
    def __mul__(self, complex_number):
        real = self.real*complex_number.real-self.imag*complex_number.imag
        imag = self.real*complex_number.imag + self.imag*complex_number.real
        output = ComplexNumbers(real, imag)
        return output
    def __repr__(self):
        return f'La parte real es {self.real} y la parte imaginaria es {self.imag}'

class TriplexNumbers(ComplexNumbers):   # Inheritance from parent class 'ComplexNumbers'
    def __init__(self, real, imag, tres):
        super().__init__(real, imag)
        self.tres = tres
    def __repr__(self):
        return f'La parte real es {self.real}, la parte imaginaria es {self.imag} y la parte tres es {self.tres}'
    def __add__(self, number):
        if not isinstance(number, TriplexNumbers):  #If it receives a complex number, then it executes the parent's __add__
            output = super().__add__(number)
        else:
            output = TriplexNumbers(
                self.real+number.real,
                self.imag+number.imag,
                self.tres+number.tres)   
        return output
