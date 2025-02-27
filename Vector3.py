from math import sqrt

class Vector3:
    def __init__(self, x = None, y: float = None, z: float = None):
        self.set(x, y, z)

    def set(self, x, y: float = None, z: float = None) -> None:
        r = [0, 0, 0]
        try:
            for i in range(len(x)):
                r[i] = x[i]
                if i >= 2:
                    break
        except:
            if x: r[0] = x
            if y: r[1] = y
            if z: r[2] = z

        self.x = r[0]
        self.y = r[1]
        self.z = r[2]

    def get(self) -> tuple[float]:
        return (self.x, self.y, self.z)

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        l = self.length()
        if l == 0: return self
        return Vector3(self.get()) / self.length()

    def __add__(self, other):
        r = list(self.get())
        if type(other) == type(self):
            a = other.get()
        else:
            a = [other] * 3
        for i in range(3):
            r[i] += a[i]
        return Vector3(r)

    def __sub__(self, other):
        r = list(self.get())
        if type(other) == type(self):
            a = other.get()
        else:
            a = [other] * 3
        for i in range(3):
            r[i] -= a[i]
        return Vector3(r)

    def __mul__(self, other):
        r = list(self.get())
        if type(other) == type(self):
            r[0] = self.y * other.z - self.z * other.y
            r[1] = 0 - (self.x * other.z - self.z * other.x)
            r[2] = self.x * other.y - self.y * other.x
        else:
            for i in range(3):
                r[i] *= other
        return Vector3(r)

    def __truediv__(self, other):
        r = list(self.get())
        if type(other) == type(self):
            return Vector3()
        else:
            for i in range(3):
                r[i] /= other
        return Vector3(r)

    def __pow__(self, power, modulo=None):
        if type(self) == type(power):
            return self.x * power.x + self.y * power.y + self.z * power.z
        return Vector3()