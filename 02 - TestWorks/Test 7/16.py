from functools import lru_cache
@lru_cache(None)
def F(n):
   if n == 1:
      return 1
   if n > 1:
      return n * F(n-1)
   
for i in range(2,2025):
   F(i)

print(((F(2025)//25)+F(2024))//F(2023))
