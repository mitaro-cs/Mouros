def f(a,b,c,d):
    return (f'{bin(a)[2:].zfill(8)}.{bin(b)[2:].zfill(8)}.{bin(c)[2:].zfill(8)}.{bin(d)[2:].zfill(8)}')

print(f(255,255,248,0))
print(f(204,16,168,0))