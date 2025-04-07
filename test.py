from math import log2
from math import ceil

def tobyte(a: int, n: int = -1):
    r = str(bin(a))[2:]
    if n == -1: return r
    if len(r) >= n: return r
    return (n-len(r)) * '0' + r
def xor(a: int, b: int) -> int: return int((a or b) and (not (a and b)))

def g(n: str):
    l = len(n)
    r = n[0]
    for i in range(1, l):
        r = r + str(xor(int(n[i-1]), int(n[i])))
    return r

for i in range(16):
    a = g(tobyte(i))
    tmp = str(i)
    if len(tmp) == 1: tmp = '0' + tmp
    tmp = tmp + ' ' + (ceil(log2(16))-len(a)) * '0' + a
    print(tmp)