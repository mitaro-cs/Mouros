for n in range(4,10000):
    s = "1" + "9"*n
    while "19" in s or "399" in s or "999" in s:
        if "19" in s:
            s = s.replace("19","9",1)
        if "399" in s:
            s = s.replace("399","91",1)
        if "999" in s:
            s = s.replace("999","3",1)
    res = s.count("1") + 3*(s.count("3")) + 9*(s.count("9"))
    if res == 33:
        print(n)
        break
