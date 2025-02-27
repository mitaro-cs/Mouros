file = open("17var01.txt")
numbers = [int(i) for i in file]
for i in range(len(numbers)):
   min_elm = min(numbers)
   if numbers[i] % 27 == min_elm or numbers[i+1] % 27 == min_elm:


      
