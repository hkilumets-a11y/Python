def eelarve(kylaliste_arv):

    return kylaliste_arv *10 + 55

kutsutud = int(input("Mitu inimest on kutsutud?"))
tulemas = int(input("Mitu inimest tuleb?"))

max_eelarve = eelarve(kutsutud)
min_eelarve = eelarve(tulemas)

print("Maksimaalne eelarve:", max_eelarve, "eurot")
print("Minimaalne eelarve:", min_eelarve, "eurot")
