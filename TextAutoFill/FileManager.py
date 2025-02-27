from math import floor
import os

path = os.getcwd() + '\\data.yml'

def __fixarg(arg: str) -> str:
    return arg.replace('.', '')

def gettabs(line: str) -> int:
    r = 0
    for i in line:
        if i != ' ': break
        r += 0.5
    return floor(r)

def checktabs(line: str, tabs: int) -> int:
    tabs = tabs * 2 - gettabs(line)
    if tabs == 0: return 0
    if tabs < 0: return -1
    return 1

def searchpath(arg: str) -> int:
    arg = __fixarg(arg)
    line = 0
    tabs = 0

    with open(path, 'r') as f:
        data = f.readlines()

    l = len(data)
    while line < l:
        text = data[line]
        ctabs = checktabs(text, tabs)
        if ctabs > 0:
            return -1
        elif ctabs == 0:
            text = text.replace(' ' * 2 * tabs, '')
            if text.split(':')[0] == arg[tabs]:
                tabs += 1
                if tabs == len(arg):
                    return line
        line += 1
    return -1

def getendpath(arg: str) -> int:
    with open(path, 'r') as f:
        data = f.readlines()

    line = searchpath(arg) + 1
    if line > len(data)-1: return line
    tabs = arg.count('.')

    while checktabs(data[line], tabs) < 0:
        line += 1
    return line

def readvalue(arg: str) -> int:
    with open(path, 'r') as f:
        data = f.readlines()

    line = searchpath(arg)

    if len(data) < line: return None

    return int(data[line].replace(' ', '').split(':')[1])

def writevalue(arg: str, value: int):
    arg = __fixarg(arg)

    with open(path, 'r') as f:
        data = f.readlines()

    sarg = ''
    tabs = 0
    for i in arg:
        parg = sarg
        if tabs == 0: sarg = i
        else: sarg = sarg + '.' + i

        line = searchpath(sarg)
        if line == -1:
            if len(arg) == tabs:
                data.insert(getendpath(sarg), ' ' * 2 * tabs + i+': '+str(value))
                return
            else:
                data.insert(getendpath(parg), ' ' * 2 * tabs + i+':\n')
        tabs += 1

    with open(path, 'w+') as f:
        f.writelines(data)

writevalue('a.d', 2)