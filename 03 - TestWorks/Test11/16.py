from functools import *
@lru_cache(None) # тут вроде это вообще не нужно

def f(n):
    if n < 3:
        return 1
    if n > 2 and n%2 != 0:
        return f(n-1) + f(n-2)
    if n > 2 and n%2 == 0:
        return #не знаю как такое записать
     
print(f(24))