for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if (not(x <= y) or (not(w) <= (not(z))) or w) == 0:
                    print(x,y,z,w)