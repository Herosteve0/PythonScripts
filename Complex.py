class Complex:
    def __init__(self, a: float = 0, b: float = 0):
        self.a = a
        self.b = b

    def read(self) -> str:
        if self.a == 0 and self.b == 0: return '(0)'

        r = ''
        if self.a != 0: r = r + str(self.a)

        if self.b != 0:
            if r != '':
                if self.b < 0: r = r + ' - '
                else: r = r + ' + '
            if abs(self.b) != 1: r = r + str(abs(self.b))
            r = r + 'i'
        return '(' + r + ')'

    def Re(self) -> float: return self.a
    def Im(self) -> float: return self.b

    def set(self, a: float = None, b: float = None) -> None:
        if a: self.a = a
        if b: self.b = b

    def __add__(self, other):
        if type(self) == type(other): return Complex(self.a + other.a, self.b + other.b)
        return Complex(self.a + other, self.b)

    def __sub__(self, other):
        if type(self) == type(other): return Complex(self.a - other.a, self.b - other.b)
        return Complex(self.a - other, self.b)

    def __mul__(self, other):
        if type(self) == type(other): return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
        return Complex(self.a * other, self.b * other)

    def __truediv__(self, other):
        if type(self) == type(other):
            return Complex((self.a * other.a + self.b * other.b), (self.b * other.a - self.a * other.b)) / (other.a ** 2 + other.b ** 2)
        return Complex(self.a / other, self.b / other)

    def __pow__(self, power, modulo=None):
        if type(self) == type(other):
            return Complex()
        return Complex()

a = iNum(1, 3)
b = iNum(6, 2)
c = iNum(0, 1)