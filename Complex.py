from math import sqrt
from math import atan2
from math import sin
from math import cos

class Complex:
    def __init__(self, a: float = 0, b: float = 0):
        self.a = round(a, 10)
        self.b = round(b, 10)

    def set(self, a: float = None, b: float = None) -> None:
        if a: self.a = a
        if b: self.b = b

    def read(self) -> str:
        if self.a == 0 and self.b == 0: return '(0)'

        r = ''
        if self.a != 0: r = r + str(self.a)

        if self.b != 0:
            if self.b < 0: r = r + '-'
            elif r != '': r = r + '+'
            if abs(self.b) != 1: r = r + str(abs(self.b))
            r = r + 'i'
        return '(' + r + ')'

    def Re(self) -> float: return self.a
    def Im(self) -> float: return self.b

    def Argument(self) -> float: return atan2(self.b, self.a)

    def __abs__(self): return sqrt(self.a**2 + self.b**2)
    def Length(self) -> float: return abs(self)

    def Conjudate(self): return Complex(self.a, -self.b)

    def toPolar(self): return (abs(self), self.Argument())

    @staticmethod
    def fromPolar(r: float, theta: float): return r * Complex(cos(theta), sin(theta))

    def __add__(self, other):
        if type(self) == type(other): return Complex(self.a + other.a, self.b + other.b)
        return Complex(self.a + other, self.b)

    def __radd__(self, other): return self.__add__(other)

    def __sub__(self, other):
        if type(self) == type(other): return Complex(self.a - other.a, self.b - other.b)
        return Complex(self.a - other, self.b)

    def __rsub__(self, other): return self.__sub__(other)

    def __mul__(self, other):
        if type(self) == type(other): return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
        return Complex(self.a * other, self.b * other)

    def __rmul__(self, other): return self.__mul__(other)

    def __truediv__(self, other):
        if type(self) == type(other):
            return Complex((self.a * other.a + self.b * other.b), (self.b * other.a - self.a * other.b)) / (other.a ** 2 + other.b ** 2)
        return Complex(self.a / other, self.b / other)

    def __rtruediv__(self, other):
        return other * Complex(self.a, -self.b) / (self.a ** 2 + self.b ** 2)

    def __pow__(self, power, modulo=None):
        n1 = self.toPolar()
        if type(self) == type(power):
            return Complex()
        return Complex.fromPolar(n1[0] ** power, power * n1[1])

a = Complex(1, 3)
b = Complex(6, -2)
c = Complex(0, 1)

print((c**2).read())