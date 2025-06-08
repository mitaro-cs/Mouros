for x in "0123456789ABCDEFGHIJKLMNO":
    sum25 = int(f"11353{x}12",25) + int(f"135{x}21",25)
    if sum25 % 24 == 0:
        print("Наибольшее",x)
        print("Частное от деления sum25 на 24 =",sum25//24)
