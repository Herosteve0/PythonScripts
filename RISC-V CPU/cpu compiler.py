"""
0000: add
  reg: rd = s1 + (rs2 + imm[7:0])
  imm: rd = rs1 + imm[10:0]
0001: sub
  reg: rd = rs1 - (rs2 + imm[7:0])
  imm: rd = rs1 - imm[10:0]
0010: and
  reg: rd = rs1 and (rs2 + imm[7:0])
  imm: rd = rs1 and imm[10:0]
0011: or
  reg: rd = rs1 or (rs2 + imm[7:0])
  imm: rd = rs1 or imm[10:0]
0100: xor
  reg: rd = rs1 xor (rs2 + imm[7:0])
  imm: rd = rs1 xor imm[10:0]
0101: nand
  reg: rd = rs1 nand (rs2 + imm[7:0])
  imm: rd = rs1 nand imm[10:0]
0110: srl
  reg: rd = rs1 << (rs2 + imm[7:0])
  imm: rd = rs1 << imm[10:0] (8 will fully clear the register)
0111: sll
  reg: rd = rs1 >> (rs2 + imm[7:0])
  imm: rd = rs1 >> imm[10:0] (8 will fully clear the register)
1000: lw
  reg: rd = memory at address (rs1 + imm[7:0])
  imm: rd = memory at address imm[10:0]
1001: sw
  reg: memory at address (rs2 + imm[7:0]) = rs1
  imm: memory at address imm[10:0] = rs1
1010: j
  reg: pc = (rs1 + imm[7:0])
  imm: pc = imm[10:0]
1011:
  reg:
  imm:
1100: beq
  reg: pc = imm[7:0], if (rs1 = rs2)
  imm: pc = imm[10:4], if (rs1 = imm[3:0]
1101: blt
  reg: pc = imm[7:0], if (rs1 < rs2)
  imm: pc = imm[10:4], if (rs1 < imm[3:0])
1110: rlt
  reg: rd = int(rs1 < rs2)
  imm: rd = int(rs1 < imm[10:0])
1111: stop
  ends the instructions
"""
sim_cmdlist_path = "C:/Users/U S E R/AppData/LocalLow/SebastianLague/Digital-Logic-Sim/Projects/RISC-V CPU/Chips/INSTRUCTION MEMORY.json"

cmds = [
    'add', 'sub', 'and', 'or', 'xor', 'nand', 'srl', 'sll',
    'lw', 'sw', 'j', 'jr', 'beq', 'blt', 'req', 'stop']
othercmds = [
    'li'
]

instruction_bit_size = 24

cmdlist = []

def numberToBits(n: int, length: int = 4) -> str:
    return bin(n).removeprefix('0b').rjust(length, '0')

def CommandToCode(cmd: str) -> str:
    try:
        return numberToBits(cmds.index(cmd))
    except:
        raise ValueError(f"Error: Could not understand command \'{cmd}\'")

def RegisterToCode(reg: str) -> str:
    return numberToBits(int(reg.removeprefix('x')))

def ChangeSimulationCommands():
    with open(sim_cmdlist_path, 'r') as f:
        data = f.readlines()
    pos = -1
    flag = False
    for i in range(len(data)):
        if "ROM 256Γ—16" in data[i]:
            flag = True
        elif "InternalData" in data[i] and flag:
            pos = i
            break
    if pos == -1: raise ValueError("Error: Simulation ROM not found.")

    text = data[pos].split(':')
    rom = text[1].removeprefix('[').removesuffix(']\n').split(',')
    rom = [int(i) for i in rom]

    c = 0
    for i in range(0, len(rom), 2):
        if len(cmdlist) <= c: break
        rom[i] = int(cmdlist[c][0:16], 2)
        rom[i+1] = int(cmdlist[c][16:instruction_bit_size], 2)
        c += 1
    data[pos] = text[0] + ':' + str(rom).replace(' ', '') + '\n'

    with open(sim_cmdlist_path, 'w+') as f:
        f.writelines(data)

def ShowResultCode():
    for i in range(len(cmdlist)):
        bits = [x for x in cmdlist[i]]
        bits.reverse()

        text = [
            ''.join(bits[0:4]),
            ''.join(bits[4:8]),
            bits[8],
            ''.join(bits[9:12]),
            ''.join(bits[12:16])
        ]

        if bits[8] == '1':
            text.append(''.join(bits[16:24]))
        else:
            text.append(''.join(bits[16:20]))
            text.append(''.join(bits[20:24]))

        print(f"{i}: {' '.join(text)}")

def PseudoCommandsToCommands(cmd: str, args):
    r = []
    if cmd == 'li':
        r.append(['srl', True, args[0], args[0], 8])
        r.append(['add', True, args[0], args[0], args[1]])
    return r

def WriteInBitArray(og: str, val: str, fr: int, to: int) -> str:
    end = instruction_bit_size - 1 - fr
    start = instruction_bit_size - 1 - to

    if start > end:
        raise ValueError("Error: Invalid from to in bit array insertion.")
    val = val.rjust(end-start+1, '0')

    text = [x for x in og]

    c = 0
    for i in range(start, end + 1):
        text[i] = val[c]
        c += 1
    return ''.join(text)

def ReadCodeFile():
    with open("code", 'r') as f:
        return f.read().split('\n')

def EncodeCodeFile(rawcode):
    global cmdlist

    commands = []
    for i in rawcode:
        if i == '': continue
        tmp = i.split(' ', 1)
        args = tmp[1].split(', ')
        cmd = tmp[0]

        if cmd in othercmds:
            commands = commands + PseudoCommandsToCommands(cmd, args)
        else:
            commands.append([cmd.removesuffix('i'), cmd.endswith('i')] + args)

    commands.append(['stop'])

    cmdlist = []
    for i in commands:
        v = '0' * instruction_bit_size
        v = WriteInBitArray(v, CommandToCode(i[0]), 0, 3)
        if len(i) > 2: v = WriteInBitArray(v, RegisterToCode(i[2]), 4, 7)
        if len(i) > 1:
            v = WriteInBitArray(v, str(int(i[1])), 8, 8)
            if i[1]:
                v = WriteInBitArray(v, numberToBits(int(i[4]), 8), 16, 23)
            else:
                v = WriteInBitArray(v, RegisterToCode(i[4]), 16, 19)
                v = WriteInBitArray(v, '0000', 20, 23)
        if len(i) > 3: v = WriteInBitArray(v, RegisterToCode(i[3]), 12, 15)

        cmdlist.append(v)

    return cmdlist

#EncodeCodeFile(ReadCodeFile())
#ShowResultCode()
#ChangeSimulationCommands()