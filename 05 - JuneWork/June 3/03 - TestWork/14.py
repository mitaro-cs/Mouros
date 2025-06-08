for x in "0123456789ABCDEFG":
    s = int(f"5432{x}67",17) + int(f"302{x}",17) 
    if s % 19 == 0:
        print(x,s) 