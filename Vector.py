from math import sqrt

class Vector:
    def __init__(self, *nums: tuple[float]) -> None:
        self.set(nums)

    def __fixtuple(self, nums: tuple[float]) -> tuple[float]:
        while type(nums) == type(nums[0]):
            nums = nums[0]
            if len(nums) == 0:
                return ()
        return nums

    def set(self, *nums: tuple[float]) -> None:
        self.coords = self.__fixtuple(nums)

    def get(self) -> tuple[float]:
        return self.coords

    def length(self) -> float:
        if len(self.coords) == 0: return 0
        s = 0
        for i in self.coords:
            s += i ** 2
        return sqrt(s)

    def normalize(self):
        l = self.length()
        if l == 0: return self
        return Vector(self.coords) / l

    def __add__(self, other):
        r = list(self.get())
        l = len(self.coords)
        if type(other) == type(self):
            a = other.get()
            limit = len(other.get())
        else:
            a = [other] * l
            limit = l
        for i in range(l):
            if i >= limit:
                break
            r[i] += a[i]
        return Vector(tuple(r))

    def __sub__(self, other):
        r = list(self.get())
        l = len(self.coords)
        if type(other) == type(self):
            a = other.get()
            limit = len(other.get())
        else:
            a = [other] * l
            limit = l
        for i in range(l):
            if i >= limit:
                break
            r[i] -= a[i]
        return Vector(tuple(r))

    def __mul__(self, other):
        r = list(self.get())
        l = len(self.coords)
        if type(other) == type(self):
            return Vector()
        else:
            for i in range(l):
                r[i] *= other
        return Vector(tuple(r))

    def __truediv__(self, other):
        r = list(self.get())
        l = len(self.coords)
        if type(other) == type(self):
            return Vector()
        else:
            for i in range(l):
                r[i] /= other
        return Vector(tuple(r))

    def __pow__(self, power, modulo=None):
        if type(self) == type(power):
            l = min(len(self.get()), len(power.get()))
            if l == 0: return 0
            s = 0
            for i in range(l):
                s += self.coords[i] * power.coords[i]
            return s
        return Vector()