import sys
sys.setrecursionlimit(5000)
def f(n):
   if n == 1:
      return 1
   if n > 1:
      return n +f(n-1)
   
print(f(3000) - f(2000))