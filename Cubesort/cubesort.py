from time import time
from random import randint as rnd
from random import shuffle
from sys import setrecursionlimit, getrecursionlimit
setrecursionlimit(10000)

def merge(a: list[str], b: list[str], enddata: str):
    i = j = 0
    c = []

    while i < len(a) and j < len(b):
        if CompareState(a[i], enddata) >= CompareState(b[j], enddata):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i == len(a):
        for j in b[j:]:
            c.append(j)
    else:
        for i in a[i:]:
            c.append(i)

    return c
def msort(a: list[str], enddata: str):
    if len(a) <= 1: return a

    mid = len(a) // 2
    left = msort(a[:mid], enddata)
    right = msort(a[mid:], enddata)
    return merge(left, right, enddata)

def GenerateBlocks(n: int = rnd(0, 26)) -> list[str]:
    tmp = []
    i = 0
    while i < n:
        j = rnd(1, n-i)
        a = [chr(i+65) for i in range(i, i+j)]
        shuffle(a)
        tmp.append(''.join(a))
        i += j

    shuffle(tmp)
    return ' '.join(tmp)

errors = ["Force Break", "No path found"]

def Visualize(data: str) -> None:
    rows = data.split(' ')

    max = 0
    for i in rows:
        l = len(i)
        if l > max:
            max = l

    print()
    l = len(rows)
    for i in range(max, 0, -1):
        tmp = ['', '', '']
        for j in range(l):
            if len(rows[j]) <= i-1:
                for k in range(3): tmp[k] = tmp[k] + '       '
            else:
                tmp[0] = tmp[0] + '┌─────┐'
                tmp[1] = tmp[1] + '│  ' + rows[j][i-1].upper() + '  │'
                tmp[2] = tmp[2] + '└─────┘'
        for j in range(3): print(tmp[j])
    print()

def GetTops(data: str) -> list[str]:
    if len(data) == 0: return []
    r = [data[-1]]
    for i in range(len(data)):
        if data[i] == ' ':
            r.append(data[i-1])
    return r

def CalcPossibleActions(data: str) -> str:
    rows = data.split(' ')
    l = len(rows)
    movable = GetTops(data)

    r = []
    for c in movable:
        tmp = FixState(data.replace(c, '_'))
        for i in range(l):
            if c in rows[i]: continue
            tmp1 = tmp.split(' ')
            tmp1[i] = tmp1[i] + c
            r.append(FixState(' '.join(tmp1).replace('_', '')))
        if c not in rows: r.append(FixState(tmp.replace('_', '') + ' ' + c))

    return r

def FixState(state: str) -> str:
    while '  ' in state:
        state = state.replace('  ', ' ')
    state = state.removesuffix(' ').removeprefix(' ')
    return state

def CompareState(data: str, enddata: str) -> int:
    blocks = len(enddata.replace(' ', ''))
    correct = mistakes = 0

    rows = sorted(data.split(' '))
    endrows = sorted(enddata.split(' '))

    l = len(rows)
    el = len(endrows)

    for i1 in range(l):
        for i2 in range(el):
            loops = min(len(rows[i1]), len(endrows[i2]))
            for j in range(loops):
                if rows[i1][j] != endrows[i2][j]: break
                correct += 1

    return correct/blocks*100

def printstateinfo(state: list[str]):
    a = msort(CalcPossibleActions(state[0]), state[1])
    tmp = []
    for i in a:
        tmp.append(CompareState(i, state[1]))
    print(state)
    print(a)
    print(tmp)
    print()

def solve(state: list[str], oldmemory: list[str] = [], count: int = 0):
    cstate = FixState(state[0])
    c = msort(CalcPossibleActions(cstate), state[1])

    memory = oldmemory.copy()
    memory.append(cstate)

    cmp = ' '.join(sorted(state[1].split(' ')))
    cmp1 = ' '.join(sorted(cstate.split(' ')))
    if cmp == cmp1: return [cstate, count, memory]

    if count == 1000:
        return [errors[0], count, memory]

    printstateinfo(state)

    for i in c:
        if i in memory: continue
        tmp = solve([i, state[1]], memory, count+1)
        cmp1 = ' '.join(sorted(tmp[0].split(' ')))
        if cmp == cmp1:
            return tmp
    return [errors[1], count, memory]

n = 10
if n == -1:
    d = ["cba ed", "ae c db"]
else:
    if n == 0: n = rnd(0, 26)
    s = GenerateBlocks(n)
    f = GenerateBlocks(n)
    d = [s, f]

print("Problem:", d[0], "→", d[1])
starttime = time()
a = solve(d)

print("Final result:", a[0])
print("Steps required:", a[1])
print("Steps took:", a[2])
print("Time elapsed", round(time() - starttime, 4))

for i in a[2]: Visualize(i)