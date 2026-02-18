def pronksikarva_summa(muntide_list):
    # Summeerib ainult väärtused 1, 2 ja 5
    summa = 0
    for munt in muntide_list:
        if munt in [1, 2, 5]:
            summa += munt
    return summa

def pronksikarva_programm():
    failinimi = input("Sisesta faili nimi, kus on müntide väärtused: ")
    muntide_väärtused = []
    
    try:
        with open(failinimi, "r") as fail:
            for rida in fail:
                rida = rida.strip()
                if rida.isdigit():
                    muntide_väärtused.append(int(rida))
    except FileNotFoundError:
        print("Faili ei leitud. Palun kontrolli faili nime ja tee uuesti.")
        return
    
    summa = pronksikarva_summa(muntide_väärtused)
    print(f"Pronksikarva sentide summa on: {summa}")

pronksikarva_programm()
