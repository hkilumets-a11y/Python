def tervitus(n):
    print(f"Võõrustaja: \"Tere!\"")
    print(f"Täna {n}. kord tervitada, mõtiskleb võõrustaja.")
    print(f"Külaline: \"Tere, suur tänu kutse eest!\"")
    print()  

def tervituste_programm():
    kylaliste_arv = int(input("Mitu külalist on? "))
    for i in range(1, kylaliste_arv + 1):
        tervitus(i)

tervituste_programm()
