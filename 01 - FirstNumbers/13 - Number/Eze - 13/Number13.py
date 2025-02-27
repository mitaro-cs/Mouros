# # Первый вариант
# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
# c = int(input("Введите число 3: "))
# d = int(input("Введите число 4: "))
# print(bin(a)[2:],bin(b)[2:],bin(c)[2:],bin(d)[2:],sep = ".")

# Второй вариант
def f(a,b,c,d):
    return (f'{bin(a)[2:].zfill(8)}.{bin(b)[2:].zfill(8)}.{bin(c)[2:].zfill(8)}.{bin(d)[2:].zfill(8)}')

print(f(255,255,0,0))
print(f(203,153,0,0))