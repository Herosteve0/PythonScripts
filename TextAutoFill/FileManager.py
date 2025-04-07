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
    return tabs - gettabs(line)

def searchpath(arg: str, line: int = 0) -> int:
    arg = __fixarg(arg)
    if arg == '':
        return -1
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
                if tabs < len(arg)-1:
                    tabs += 1
                if tabs == len(arg)-1:
                    return line
        line += 1
    return -1

def getendpath(arg: str, line: int = 0) -> int:
    with open(path, 'r') as f:
        data = f.readlines()

    line = searchpath(arg, line) + 1
    l = len(data)-1
    if line > l: return line
    tabs = arg.count('.')

    while checktabs(data[line], tabs) < 0:
        line += 1
        if line > l: break
    return line

def readvalue(arg: str) -> int:
    with open(path, 'r') as f:
        data = f.readlines()

    line = searchpath(arg)
    print(line)

    if len(data) < line: return None

    return int(data[line].replace(' ', '').split(':')[1])

def insertvalue(data: list[str], line: int, tabs: int, arg: str, value: int = None) -> list[str]:
    #print(line)
    tmp = ' ' * 2 * tabs + arg
    if value is not None:
        data.insert(line, tmp + ': ' + str(value))
    else:
        data.insert(line, tmp + ':\n')
    return data

def writevalue(arg: str, value: int):
    arg = __fixarg(arg)
    if arg == '':
        return

    with open(path, 'r') as f:
        data = f.readlines()

    sarg = ''
    line = 0
    tabs = 0
    for i in arg:
        parg = sarg
        if tabs == 0: sarg = i
        else: sarg = sarg + '.' + i

        if searchpath(sarg, line) == -1:
            if len(arg)-1 == tabs:
                data = insertvalue(data, getendpath(parg, line), tabs, i, value)
                break
            else:
                line = getendpath(sarg, line)
                data = insertvalue(data, line, tabs, i)
        else:
            line = getendpath(sarg, line)
        print(line)
        tabs += 1

    with open(path, 'w+') as f:
        f.writelines(data)

print(readvalue('a.a.a.d'))
#writevalue('a.d.d', 2)