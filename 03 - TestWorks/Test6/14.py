for x in "0123456789ABCDEFGHIJKLM":
    s = (int(f"2{x}{x}341011",23) + int(f"220{x}4",23) + int(f"110{x}6",23))
    if s % 22 == 0:
        print(s//22)
        break
    




