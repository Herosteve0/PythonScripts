def LetterToNumber(a: chr) -> int:
    r = ord(a)-65
    if r > 26: r -= 6
    if r < 0 or r >= 52: return -1
    return r

def NumberToLetter(a: int) -> chr:
    if a < 0 or a >= 52: return chr(0)
    r = a+65
    if a >= 26: r += 6
    return chr(r)

print(ord('\n'))
print(97+25)