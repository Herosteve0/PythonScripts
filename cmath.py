from math import fmod
from math import exp

def unevenround(x: float, r: list[float]) -> float:
    # r1 * round((x - r2) / r1) + r2

    for i in range(len(r)-1):
        r1 = r[i]-r[i+1]      # difference
        r2 = fmod(r[i], r1)   # offset
        if not r[i] <= x <= r[i+1]:
            continue
        return r1 * round((x - r2) / r1) + r2
    return 0

def sigmoid(x: float) -> float:
    return 1 / (1 + exp(-x))