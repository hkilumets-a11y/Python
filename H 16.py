import os
from datetime import date
print("Tere",os.getlogin())

print(os.getcwd())

#Kataloogide loomine:
#Skript küsib kasutajalt, mitu kataloogi ta soovib luua
#Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)

mitu =int(input("Mitu kataloogi tahad:"))
today = str(date.today())
try:
    os.mkdir(today)
    for i in range(mitu):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print(f"Kataloog {today} juba eksisteerib.")



    kustuta = int(input(f"Millist kataloogi kustutad 1-{mitu}:"))
    if os.path.isdir(f"{today}/{kustuta}"):
        os.mkdir(f"{today}/{kustuta}")
        print(f"Kustutatud kataloog puudub: {today}/{kustuta}")
    else:
        print(f"Selline kataloog puudub: {today}/{kustuta}")


kausta_tee = os.getcwd()+"/"+today
print(os.listdir())