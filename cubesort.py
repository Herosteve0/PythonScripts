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
        tmp = ''
        for j in range(l):
            if len(rows[j]) <= i-1:
                tmp = tmp + '   '
            else:
                tmp = tmp + ' ' + rows[j][i-1].upper() + ' '
        print(tmp)

def CalcPossibleActions(data: str) -> str:
    rows = data.split(' ')
    movable = []
    l = len(rows)
    for i in range(l):
        if len(rows[i]) <= 0: continue
        movable.append(rows[i][-1])

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
    correct = 0

    rows = sorted(data.split(' '))
    endrows = sorted(enddata.split(' '))

    l = len(rows)
    el = len(endrows)

    loop1 = min(l, el)
    for i in range(loop1):
        loop2 = min(len(rows[i]), len(endrows[i]))
        for j in range(loop2):
            if rows[i][j] != endrows[i][j]:
                break
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

    #printstateinfo(state)

    for i in c:
        if i in memory: continue
        tmp = solve([i, state[1]], memory, count+1)
        cmp1 = ' '.join(sorted(tmp[0].split(' ')))
        if cmp == cmp1:
            return tmp
    return [errors[1], count, memory]


#a = solve(["cba ed", "ae c db"])

n = rnd(0, 26)
s = GenerateBlocks(n)
f = GenerateBlocks(n)
print("Problem:", s, "→", f)

starttime = time()
a = solve([s, f])

print("Final result:", a[0])
print("Steps required:", a[1])
print("Steps took:", a[2])
print("Time elapsed", round(time() - starttime, 4))