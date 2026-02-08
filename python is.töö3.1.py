fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []
aasta = int(input("Mis aasta 2011-2803"))
for rida in fail:
    vastuvõetud.append(int(rida))
print(vastuvõetud[aasta-2011])




fail.close()