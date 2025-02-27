def is_prime(n):
   d = 2
   while d**2 <= n:
      if n % d == 0:
         return False
      d += 1
   return True

def prime_factors(n):
   d = 2
   numbers = []
   while d**2 < n:
      if n % d == 0:
         if is_prime(d):
            numbers.append(d)
         if is_prime(n//d):
            numbers.append(n//d)
      d += 1
   if d**2 == n and is_prime(d):
      numbers.append(n)      
   return numbers

for num in range(326782, 965324 + 1):
    factors = prime_factors(num)
    if len(factors) < 3:
        continue 
    for i in range(len(factors)):
        for j in range(i + 1, len(factors)):
            for k in range(j + 1, len(factors)):
                a, b, c = factors[i], factors[j], factors[k]
                if a * b * c == num and c - a <= 12:
                    print(num, c - a)
                    break
